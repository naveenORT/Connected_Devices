'''
Created on Jan 23, 2020
@author: Naveen Rajendran
'''
import random
from labs.common.SensorData import SensorData
from labs.module02.SmtpClientConnector import smtpconnect
import time
import threading
import logging


class temperaturegen(threading.Thread):
   
    data_object = SensorData()
    
    def __init__(self, max_sample, alertDiff):
        threading.Thread.__init__(self)  # Invoking Thread Function
        self.setDaemon(True)
        self.max_sample = max_sample
        self.alertDiff = alertDiff
    
    def getSensorData(self):
        return random.randrange(0, 30, 1)  # Generating Temperature Values with frequency of 1

    def sendNotification(self):  # Function to Publish Alerts As Mail
        
        smtp_object = smtpconnect()    
        message = "\n Time Recorded : " + (str)((self.data_object.gettimestamp())) + "\n Current : " + (str)(self.data_object.getcurvalue()) + "\n Average : " + (str)(self.data_object.getavgvalue()) + "\n Samples : " + (str)(self.data_object.getsamplecount()) + "\n Minimum : " + (str)(self.data_object.getminvalue()) + "\n Maximum : " + (str)(self.data_object.getcurvalue())
        smtp_object.publishMessage("Temperature Alert", message)
    
    def run(self):
        
        while temperaturegen.isDaemon(self):    
            
            emulated_temperature = self.getSensorData() 
            self.data_object.addValue(emulated_temperature)
            
            if (abs(self.data_object.curValue - self.data_object.avgValue) >= self.alertDiff): #Checking for Deviation
                logging.info('\n Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')
                self.sendNotification()
            time.sleep(3)
            self.max_sample -= 1        
            
            if self.max_sample == 0:
                return
    
