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
import time

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
        t_cpu = self.get_cpu_temp()
        h = sense_hat.get_humidity()
        p = sense_hat.get_pressure()

        # calculates the real temperature compesating CPU heating
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        t_corr = self.get_smooth(t_corr)
        
        return  t_corr  # Generating Temperature Values with frequency of 1

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

    # get CPU temperature
    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return(t)

    # use moving average to smooth readings
    def get_smooth(self,x):
        if not hasattr(self.get_smooth, "t"):
            self.get_smooth.t = [x, x, x]
        self.get_smooth.t[2] = self.get_smooth.t[1]
        self.get_smooth.t[1] = self.get_smooth.t[0]
        self.get_smooth.t[0] = x
        xs = (self.get_smooth.t[0] + self.get_smooth.t[1] + self.get_smooth.t[2]) / 3
        return(xs)
    
