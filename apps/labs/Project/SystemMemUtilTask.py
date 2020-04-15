'''
Created on Jan 14, 2020

@author: Naveen Rajendran
'''
import psutil

class memutil:    

    def _init_(self): 
        self.getSensorData()  # Default Constructor
    
    def getSensorData(self):
        m = psutil.virtual_memory().percent  # Getting value from psutil library
        return m

