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
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.max_sample = max_sample
        self.alertDiff = alertDiff
    
    def getSensorData(self):
        return random.randrange(0, 30, 1)

    def sendNotification(self):
        
        smtp_object = smtpconnect()    
        message = ("Current Value:", self.data_object.getcurvalue(),  
                   "Average Value:", self.data_object.getavgvalue() , 
                   "Samples:",       self.data_object.getsamplecount() ,  
                   "Min:",           self.data_object.getminvalue() , 
                   "Max:",           self.data_object.getcurvalue())
        
        smtp_object.publishMessage("Temperature Alert:", message)
        
    
    def run(self):
        
        while temperaturegen.isDaemon(self):    
            
            emulated_temperature = self.getSensorData() 
            self.data_object.addValue(emulated_temperature)
            
            if (abs(self.data_object.curValue - self.data_object.avgValue) >= self.alertDiff):
                logging.info('\n Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')
                self.sendNotification()
            time.sleep(3)
            self.max_sample -= 1        
            
            if self.max_sample == 0:
                return
    