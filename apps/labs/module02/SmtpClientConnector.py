'''
Created on Jan 23, 2020

@author: Naveen Rajendran
'''
import logging
import smtplib
from labs.common.ConfigUtil import ConfigUtil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class smtpconnect():
 
    def __init__(self):               
        self.config = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props")
        logging.info('Configuration data...\n' + str(self.config.config.sections()))
    
    def publishMessage(self, topic, data):        
        host = self.config.getValues("smtp.cloud", "host")
        port = self.config.getValues("smtp.cloud", "port")
        fromAddr = self.config.getValues("smtp.cloud", "fromAddr")
        toAddr = self.config.getValues("smtp.cloud", "toAddr")
        authToken = self.config.getValues("smtp.cloud", "authToken")
        
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = "Current temp =" + str(data)
        msg.attach(MIMEText(msgBody,"plain"))
      
        logging.info(host)      
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        msgText = msg.as_string()
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
            
