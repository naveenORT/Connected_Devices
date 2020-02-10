'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.ActuatorData import ActuatorData
from labs.module03.SimpleLedAActivator import SimpleLedActivator
import logging
from labs.module03.TempSensorAdaptorTask import data_object


class TempActuatorAdaptor():
    
    def __init__(self):
        logging.info("Actuation")     
        
        if  (data_object.getcurvalue() < 20):
            self.actuator_status = ActuatorData()
            self.actuator_status.addData("Increase Temperature", data_object.getcurvalue(), "Temperature Sensor")
            high = SimpleLedActivator(3)
            high.setBLUE()
            high.default_led()
            return
        
        if  (data_object.getcurvalue() > 20):
            self.actuator_status = ActuatorData()
            self.actuator_status.addData("Decrease Temperature", data_object.getcurvalue(), "Temperature Sensor")
            low = SimpleLedActivator(3)
            low.setRED()
            low.default_led()
            return
        else:
            return
        
    def getActuator_obj(self):
        return self.actuator_status