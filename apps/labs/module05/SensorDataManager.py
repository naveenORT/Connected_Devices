'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
import threading
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
# from labs.module05.HI2CSensorAdaptorTask import i2c_data_object
from labs.common.ActuatorDataListener import ActuatorDataListener
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
        time.sleep(1)
        self.alo = ActuatorDataListener()
        self.alo.start()
        
    '''
    * Runnable thread,to perform actuation
    '''

    def run(self):    
      
        while(True):
            if (self.alo.on_Actuator_Message() is True):
                maa = MultiActuatorAdaptor()
                maa.temp_act(self.alo.get_alo_object().sensor_value)
            else:
                continue
            time.sleep(5)
        
    '''
    * Function to create instance of MultiActuatorAdaptor class 
    '''

    def trigger_actuation(self):
            self.maa = MultiActuatorAdaptor()        

    '''
    * Standard getter function
    * Output: MultiActuatorAdaptor(object)
    '''

    def get_maaadaptor(self):   
            return self.maa 

    '''
    * Function to handle sensor data, so as to activate actuator
    * Input: SensorData(Object) 
    * Output: True or False (Boolean)
    '''    

    def handle_sensordata(self, invalue):
        self.x = invalue
        if(self.x.getActuationStae() is True):
            return True    
        if(self.x.getActuationStae() is False):
            return False

    def get_alo(self):    
        return self.alo