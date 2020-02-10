'''
Created on Feb 6, 2020
@author: Naveen Rajendra
'''
import threading
import time 
from labs.module02.SmtpClientConnector import smtpconnect
from labs.module03.TempSensorAdaptorTask import data_object
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.common.ConfigUtil import ConfigUtil

class SensorDataManager(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        SensorDataManager.setDaemon(self,True)
        self.nominal_temp = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props")
        self.temp_set_point = self.nominal_temp.getValues("device", "nominalTemp")
    
    def trigger_notification(self):
        if (data_object.getcurvalue() >= float(self.temp_set_point)):        
            self.sendNotification() 
        else: 
            return 
    def sendNotification(self):  # Function to Publish Alerts As Mail
        smtp_object = smtpconnect()    
        self.message = "\n Time Recorded : " + (str)((data_object.gettimestamp())) + "\n Current : " + (str)(data_object.getcurvalue()) + "\n Average : " + (str)(data_object.getavgvalue()) + "\n Samples : " + (str)(data_object.getsamplecount()) + "\n Minimum : " + (str)(data_object.getminvalue()) + "\n Maximum : " + (str)(data_object.getcurvalue())
        smtp_object.publishMessage("Temperature Alert", self.message)

    def run(self):
        while SensorDataManager.is_alive(self):
            self.trigger_notification()
            x = TempActuatorAdaptor()
            time.sleep(3)
    
    def getNotification_msg(self):      
        return self.message