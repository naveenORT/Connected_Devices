'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from datetime import datetime 
import logging

'''
* This python class module records or logs condition of Actuator as per the input command given by user at origin
* This class gets updated whenever a new value from sensor is obtained
'''


class ActuatorData():
    
    '''
    Default Constructor of ActuatorData class, notifies user via log message before an actuation is done
    '''
    
    def __init__(self):
        logging.info("\n")
        logging.info("Going to Perform an Actuation")  # log status to notify actuation
    
    '''
    This class function receives the input_command, sensor_value and sensor_name & sets the state of actuator based on input_command
    given by user
    '''

    def addData(self, input_command, sensor_value, sensor_name):
        
        if(sensor_name == "Temp Sensor"):
            self.sensor_name = sensor_name
            self.set_current_actuator_status(input_command)  # Setting actuator status
            self.value = sensor_value  # Store Sensor Value
            self.set_command(input_command)  # Setting input command
        
        if(sensor_name == "Humidity_API"):
            self.sensor_name = sensor_name
            self.set_current_actuator_status(input_command)
            self.value = sensor_value  # Store Sensor Value
            self.set_command(input_command)  # Setting input command
            
        if(sensor_name == "Humidity_I2C"):
            self.sensor_name = sensor_name
            self.set_current_actuator_status(input_command)
            self.value = sensor_value  # Store Sensor Value
            self.set_command(input_command)  # Setting input command
            
        logging.info("Sensor Name = " + str(self.getName()))
        logging.info("Current Value is =" + str(self.getValue()))
        logging.info("Input Command =" + self.get_command()) 
        logging.info("Current Actuator Status =" + self.get_current_actuator_status())            
    
    def setActuation_state(self, in_value):
        self.state = in_value
    
    def getActuation_state(self):
        return self.state

    '''               
    Standard getter function for command
    '''

    def get_command(self):
        return self.command
   
    '''               
    Standard getter function for sensor_name
    '''

    def getName(self):
        return self.sensor_name
    
    '''               
    Standard getter function for sensor_value
    '''

    def getValue(self):
        return self.value
    
    '''               
    Standard getter function for sensor_value
    '''

    def get_current_actuator_status(self):
        return self.status
     
    '''               
    Standard setter function for sensor_name
    '''

    def setName(self, name):   
        self.sensor_name = name
        
    '''               
    Standard setter function for input_command
    '''

    def set_command(self, input_command):
        self.command = input_command
    
    '''               
    Standard setter function for actuator_status
    '''

    def set_current_actuator_status(self, command):
        
        if command == "Increase Temperature":
            self.status = "Glowing RED"  # Set Status to RED
        
        if command == "Decrease Temperature":    
            self.status = "Glowing BLUE"  # Set Status to BLUE
        
        if command == "i2c_inbound":
            self.status = "green text message"
        
        if command == "api_inbound":
            self.status = "blue text message"
                
        if command == "temp_inbound":
            self.status = "showing api temp"
       
