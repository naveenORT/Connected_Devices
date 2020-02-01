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
    msgBody = ''
    fromAddr = ''
    toAddr = ''
    host = ''

    def __init__(self):               
        self.config = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props")
        logging.info('Configuration data...\n' + str(self.config.config.sections()))  # Constructor loading config properties from the file
    
    def publishMessage(self, topic, data):  # Publishing Mail Via SMTP
        self.host = self.config.getValues("smtp.cloud", "host")
        port = self.config.getValues("smtp.cloud", "port")
        self.fromAddr = self.config.getValues("smtp.cloud", "fromAddr")
        self.toAddr = self.config.getValues("smtp.cloud", "toAddr")
        authToken = self.config.getValues("smtp.cloud", "authToken")
        
        msg = MIMEMultipart()
        msg['From'] = self.fromAddr
        msg['To'] = self.toAddr
        msg['Subject'] = topic
        self.msgBody = " Present Status!!! " + str(data)
        msg.attach(MIMEText(self.msgBody, "plain"))
      
        logging.info(self.host)      
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(self.host, port)  # Creating SMTP server
        smtpServer.ehlo()
        smtpServer.login(self.fromAddr, authToken)  # Authentication
        msgText = msg.as_string()  # Converting to String
        smtpServer.sendmail(self.fromAddr, self.toAddr, msgText)  # Send Mail
        smtpServer.close()
     
    def getfromAddr(self):       
         return self.fromAddr

    def gettoAddr(self):       
         return self.toAddr
     
    def getmsgBody(self):
         return self.msgBody
     
    def getHost(self):
        return self.host
