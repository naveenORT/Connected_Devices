'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
import logging
from labs.module07.SenseHatLedActivator import SimpleLedActivator
import redis
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
        logging.info("Actuating")
        
    '''
    * Actuator function for temperature sensor class, actuation_status is set true when LED actuation gets completed
    '''

    def temp_act(self, input_value):        
            self.api_message = SimpleLedActivator(10)
            #self.api_message.show_api_LED(float(input_value))    
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
    
