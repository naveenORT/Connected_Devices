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
	x=SimpleLedActivator()
	x.default_led()
        if  (data_object.getcurvalue() < 20):
            self.actuator_status = ActuatorData("Increase Temperature",data_object.getcurvalue())
            high = SimpleLedActivator(3)
            high.setBLUE()
            return
        if  (data_object.getcurvalue() > 20):
            self.actuator_status = ActuatorData("Decrease Temperature",data_object.getcurvalue())
            y = self.actuator_status.get_current_actuator_status();
            low = SimpleLedActivator(3)
            low.setRED()
            return
        else:
            return
