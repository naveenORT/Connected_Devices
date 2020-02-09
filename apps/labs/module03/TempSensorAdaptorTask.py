'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
import random

data_object = SensorData()
sense_hat = SenseHat()   


class TempSensorAdaptorTask(threading.Thread):
       
    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        TempSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    def getSensorData(self):
        t1 = sense_hat.get_temperature_from_humidity()
        t2 = sense_hat.get_temperature_from_pressure()
    
        # calculates the real temperature compesating CPU heating
        t = ((t1))/ 2
        return  t  # Generating Temperature Values with frequency of 1

    def getdata(self):
        return random.randrange(0, 30, 1)  # Generating Temperature Values with frequency of 1
    
    def run(self):    
        while TempSensorAdaptorTask.isDaemon(self):    
            environment_temperature = self.getSensorData()
            data_object.addValue(environment_temperature)
            time.sleep(5)
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return

    
