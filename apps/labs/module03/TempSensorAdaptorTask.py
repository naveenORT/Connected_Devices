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

data_object = SensorData()
sense_hat = SenseHat()   

class TempSensorAdaptorTask(threading.Thread):
       
    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        TempSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    def getSensorData(self):
        
        t_f_humidity = self.sense_hat.get_temperature_from_humidity()
        cpu = sense_hat.get_cpu_temp()
        pres = sense_hat.get_pressure()
        hum = sense_hat.get_humidity()
        # calculates the real temperature compensating CPU heating
        correct_temp = t_f_humidity - ((cpu - t_f_humidity)/1.5)
        print("t_f_humidity=%.1f  cpu=%.1f  correct_temp=%.1f  hum=%d  pres=%d" % (t_f_humidity, cpu, correct_temp, round(hum), round(pres)))
        return  correct_temp    # Generating Temperature Values with frequency of 1

    def getdata(self):
        return random.randrange(0, 30, 1)  # Generating Temperature Values with frequency of 1
    
    def run(self):    
        while TempSensorAdaptorTask.isDaemon(self):    
            environment_temperature = self.getdata()
            data_object.addValue(environment_temperature)
            time.sleep(2)
            self.max_sample -= 1        
            
            if self.max_sample == 0:
                return
    