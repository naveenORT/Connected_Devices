'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
import threading
import time 
from labs.module02.SmtpClientConnector import smtpconnect
from labs.module03.TempSensorAdaptorTask import data_object
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
class SensorDataManager(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        SensorDataManager.setDaemon(self,True)
    
    def trigger_notification(self):
        if (abs(data_object.getcurvalue() - data_object.getavgvalue()) > 5):        
            self.sendNotification() 

    def sendNotification(self):  # Function to Publish Alerts As Mail
        smtp_object = smtpconnect()    
        message = "\n Time Recorded : " + (str)((data_object.gettimestamp())) + "\n Current : " + (str)(data_object.getcurvalue()) + "\n Average : " + (str)(data_object.getavgvalue()) + "\n Samples : " + (str)(data_object.getsamplecount()) + "\n Minimum : " + (str)(data_object.getminvalue()) + "\n Maximum : " + (str)(data_object.getcurvalue())
        smtp_object.publishMessage("Temperature Alert", message)

    def run(self):
        while SensorDataManager.is_alive(self):
            self.trigger_notification()
            #TempActuatorAdaptor(data_object)                
            time.sleep(2)