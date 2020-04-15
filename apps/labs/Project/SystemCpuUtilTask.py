'''
Created on Jan 14, 2020

@author: Naveen Rajendran
'''
import psutil

class cpuutil:
    
    def _init_(self):
        self.getSensorData()  # Default_Constructor
        
    def getSensorData(self):
        c = psutil.cpu_percent(1, False)  # Reading Value from Psutil library
        return c

