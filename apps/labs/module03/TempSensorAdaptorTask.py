'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
import random

data_object = SensorData()  # class object
sense_hat = SenseHat()  # class object
"""
***********************************Module Description********************************************************************************
* In this module sense hat library function is imported for sensing temperature prevailing in external environment
* It is a threaded class which gets instantiated whenever the instance of TempSensorAdaptorClass gets created
* Functions get_temperature_from_pressure & get_temperature_from_humidity, helps to obtain read outs from GPIO pins
* Readed temperature value is passed on to instance of SensorData class & temperature values from sense hat are stored 
*************************************************************************************************************************************
"""


class TempSensorAdaptorTask(threading.Thread):
    """      
    * Constructor function which sets daemon of TempSensorAdaptorTask thread to true 
    """       

    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        TempSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    """      
    * This function uses sensehat function to extract temperature data and returns
    
    """       

    def getSensorData(self):
        t1 = sense_hat.get_temperature_from_humidity()  # Obtain temperature from humidity
        t2 = sense_hat.get_temperature_from_pressure()  # Obtain temperature from pressure
        c_temperature = ((t1 + t2)) / 2
        return  c_temperature  
    
    """      
    * Runnable thread function which uses function of SensorData to record values
    """       

    def run(self):    
        while TempSensorAdaptorTask.isDaemon(self):    
            environment_temperature = self.getSensorData()
            data_object.addValue(environment_temperature)  # Logging sensor data
            time.sleep(4)
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return
    
