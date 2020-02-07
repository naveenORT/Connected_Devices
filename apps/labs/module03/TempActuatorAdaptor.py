'''
Created on Feb 6, 2020

@author: Naveen Rajendran
'''
from labs.common.ActuatorData import ActuatorData
from labs.module03.SimpleLedAActivator import SimpleLedActivator
import logging
class TempActuatorAdaptor():
    
    
    def __init__(self,data_object):
        self.trigger_actuation(data_object)
    
    def trigger_actuation(self,data_object):        
        
        if  (data_object.getcurvalue() < data_object.getavgvalue()):   
            self.actuator_status = ActuatorData("Increase Temperature",data_object.getcurvalue)
            x = self.actuator_status.get_current_actuator_status();
            logging.info(x)
            high = SimpleLedActivator(3)
            high.setRED()
        
        if  (data_object.getcurvalue() > data_object.getavgvalue()):
            self.actuator_status = ActuatorData("Decrease Temperature",data_object.getcurvalue)
            y = self.actuator_status.get_current_actuator_status();
            logging.info(y)
            high = SimpleLedActivator(3)
            high.setRED()