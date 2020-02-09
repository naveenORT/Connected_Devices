'''
Created on Feb 6, 2020

@author: Naveen Rajendran
'''
from datetime import datetime 
import logging


class ActuatorData():
    
    def __init__(self, input_command, sensor_value):
        
        timeStamp = str(datetime.now())  # Constructor    
        self.value = sensor_value
        self.set_command(input_command)
        self.set_current_actuator_status(input_command)
        
        logging.info("Current Value is =" + str(self.getValue()))
        logging.info("Input Command ="+self.get_command()) 
                 
    
    def get_command(self):
        return self.command
   
    def getName(self):
        return self.sensor_name
    
    def getValue(self):
        return self.value
    
    def get_current_actuator_status(self):
        return self.status
     
    def setName(self, name):   
        self.sensor_name = name
        
    def set_command(self, input_command):
        self.command = input_command
    
    def set_current_actuator_status(self, command):
        
        if command == "Increase Temperature":
            self.status = "RED"
        
        if command == "Decrease Temperature":    
            self.status = "BLUE"
        
        logging.info( "Current actuator Status = " + str(self.get_current_actuator_status()))
