'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
import threading
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.SensorData import SensorData
from labs.module05.HumiditySensorAdaptorTask import humidity_data_object
from labs.module05.TempSensorAdaptorTask import data_object
#from labs.module05.HI2CSensorAdaptorTask import i2c_data_object
import time
'''
This module handles a thread that instantiates MultiActuatorAdaptor class. SensorDataManager module retrieves humidity data from 
SensorData module by importing its instances & it checks for actuation condition associated with the instance
'''

class SensorDataManager(threading.Thread):    
    '''
    * Default Constructor
    '''   
    def __init__(self):
        threading.Thread.__init__(self)    
    '''
    * Runnable thread,to perform actuation
    '''
    def run(self):    
        time.sleep(1)
        while SensorDataManager.is_alive(self):
            time.sleep(6.5)
            self.trigger_actuation()            
    '''
    * Function to create instance of MultiActuatorAdaptor class 
    '''
    def trigger_actuation(self):
            self.maa = MultiActuatorAdaptor()        
    '''
    * Standard getter function
    Output: MultiActuatorAdaptor(object)
    '''
    def get_maaadaptor(self):   
            return self.maa 
    '''
    * Function to handle sensor data, so as to activate actuator
    Input: SensorData(Object) 
    Output: True or False (Boolean)
    '''    
    def handle_sensordata(self,invalue):
        self.x = invalue
        if(self.x.getActuationStae() is True):
            return True    
        if(self.x.getActuationStae() is False):
            return False