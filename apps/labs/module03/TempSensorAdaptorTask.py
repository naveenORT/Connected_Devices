'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import logging
import time
import random
import os

data_object = SensorData()
sense_hat = SenseHat()   

class TempSensorAdaptorTask(threading.Thread):
       
    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        TempSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    def getSensorData(self):
        
        correct_temp = sense_hat.get_temperature_from_pressure()
        return  correct_temp    # Generating Temperature Values with frequency of 1

    def getdata(self):
        return random.randrange(0, 30, 1)  # Generating Temperature Values with frequency of 1
    
    def run(self):    
        while TempSensorAdaptorTask.isDaemon(self):    
            environment_temperature = self.getSensorData
            data_object.addValue(environment_temperature)
            time.sleep(2)
            self.max_sample -= 1        
            
            if self.max_sample == 0:
                return
    