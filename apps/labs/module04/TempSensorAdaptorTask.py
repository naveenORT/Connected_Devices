'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
import random

temp_data_object = SensorData()  # class object
sense_hat = SenseHat()  # class object


class TempSensorAdaptorTask(threading.Thread):

    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        TempSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    

    def getSensorData(self):
        t1 = sense_hat.get_temperature_from_humidity()  # Obtain temperature from humidity
        t2 = sense_hat.get_temperature_from_pressure()  # Obtain temperature from pressure
        sense_hat.get
        c_temperature = ((t1 + t2)) / 2
        return  c_temperature  
    

    def run(self):    
        while TempSensorAdaptorTask.isDaemon(self):    
            environment_temperature = self.getSensorData()
            temp_data_object.addValue(environment_temperature)  # Logging sensor data
            time.sleep(4)
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return
    
