'''
Created on Apr 8, 2020
@author: Naveen Rajendran
'''
import logging

class SensorData():
    
    device_id = 1001
    def __init__(self):
        logging.info("Creating Data Object")
        
    def add_Temp_Value(self,input):
        self.temperature = input 
        
    def add_Humi_Value(self,input):
        self.humidity = input 
    
    def add_Mag_Value(self,input):
        self.magflux = input
    
    def add_Cor_Value(self,input):
        self.corona_level = input
    
    def add_Res_Value(self,input):
        self.resistence = input
        
    def getTemperature(self):
        return self.temperature
    
    def getHumidity(self):
        return self.humidity
    
    def getMagFlux(self):
        return self.magflux
    
    def getCorona(self):
        return self.corona_level
    
    def getResistence(self):
        return self.resistence