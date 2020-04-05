'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
import logging
from labs.common.ActuatorData import ActuatorData
from labs.module04.HumiditySensorAdaptorTask import humidity_data_object 
from labs.module04.TempSensorAdaptorTask import data_object
from labs.module04.HI2CSensorAdaptorTask import i2c_data_object
from labs.module04.SenseHatLedActivator import SimpleLedActivator
import threading
import time

'''
* This module triggers whenever actuation state is set by SensorData class. 
* Once actuation state is set, it will call the instance of SenseHatLedActivator class and its functions show_api_message() 
  & show_i2c_message() respectively    
'''

  
class MultiActuatorAdaptor():
      
    '''
    * Constructor function which creates ActuatorData object for api sensor data & i2c sensor data 
    '''  

    def __init__(self):
        
        self.temp_actuator_status = ActuatorData()
        self.api_actuator_status = ActuatorData()
        self.i2c_actuator_status = ActuatorData()
        
        self.temp_act()
        self.humidity_api_act()
        self.humidity_i2c_act()
        
    '''
    * Actuator function for temperature sensor class, actuation_status is set true when LED actuation gets completed
    '''

    def temp_act(self):    
        if  (data_object.getActuationState() is True):
            
                self.temp_actuator_status.addData("temp_inbound", data_object.getcurvalue(), "Temperature Sensor")  # logging actuator data
                self.api_message = SimpleLedActivator(10)
                logging.info("Going to Performing Actuation")     
                self.api_message.show_api_LED(data_object.getcurvalue())
                
                if(self.api_message.get_actuation_completion is True):
                    self.temp_actuator_status.setActuation_state(True)
                return        

    '''
    * Actuator function for humidity_api sensor class, actuation_status is set true when LED actuation gets completed
    '''      

    def humidity_api_act(self): 
        humidity_data_object.setAcutationState(True)   
        if (humidity_data_object.getActuationState() is True):
        
                self.api_actuator_status.addData("api_inbound", humidity_data_object.getcurvalue(), "Humidity_API")  # logging actuator data
                self.humi_api_message = SimpleLedActivator(10)
                logging.info("Going to Performing Actuation")     
                self.humi_api_message.show_api_LED(humidity_data_object.getcurvalue())
            
                if(self.humi_api_message.get_actuation_completion() is True):
                    self.api_actuator_status.setActuation_state(True)
                return

    '''
    * Actuator function for humidity_i2c sensor class, actuation_status is set true when LED actuation gets completed
    '''

    def humidity_i2c_act(self):    
        if  (i2c_data_object.getActuationState() is True):
                self.i2c_actuator_status.addData("i2c_inbound", i2c_data_object.getcurvalue(), "Humidity_I2C")  # logging actuator data
                self.i2c_message = SimpleLedActivator(10)
                logging.info("Going to Performing Actuation")     
                self.i2c_message.show_i2c_LED(i2c_data_object.getcurvalue())
                if(self.i2c_message.get_actuation_completion() is True):
                    self.i2c_actuator_status.setActuation_state(True)
                return

    '''
    * Function to check whether LED actuation has happened or not
      Input: ActuatorData(Object)
      Output: True/False (Boolean) 
    '''

    def update_Actuator(self, invalue):   
        self.obj = invalue
        if(self.obj.getActuation_state() is True):    
            return True
        else:
            return False

    '''
    * Standard getter function to get api_actuator_status
    * Output: ActuatorData(Object)
    '''

    def getapi_actobj(self):        
        return self.api_actuator_status
    
    '''
    * Standard getter function to get i2c_actobj
    * Output: ActuatorData(Object)
    '''

    def geti2c_actobj(self):        
        return self.i2c_actuator_status
    
