'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.ActuatorData import ActuatorData
from labs.module03.SimpleLedAActivator import SimpleLedActivator
import logging
from labs.module03.TempSensorAdaptorTask import data_object
'''
***************************************************Module Description***************************************************************
* This python module is called by SensorHandlerApp class module. It has a class constructor body which contains decision making 
  statements for actuating LED s based on temperature value recorded by SensorData object
* If sensed temperature is below nominal temperature blue LED in sense hat will be glown
************************************************************************************************************************************
'''


class TempActuatorAdaptor():
    '''
    * Class constructor function which makes actuation based on current temperature value extracted from SensorData object
    * This constructor also uses functions of SimpleLedAActivator class such as setBLUE(), setRED
    '''

    def __init__(self):
        logging.info("Actuation")     
        
        if  (data_object.getcurvalue() < 20):
            self.actuator_status = ActuatorData()
            self.actuator_status.addData("Increase Temperature", data_object.getcurvalue(), "Temperature Sensor")  # logging actuator data
            high = SimpleLedActivator(3)
            high.setRED()
            #high.default_led()
            return
        
        if  (data_object.getcurvalue() > 20):
            self.actuator_status = ActuatorData()
            self.actuator_status.addData("Decrease Temperature", data_object.getcurvalue(), "Temperature Sensor")  # logging actuator data
            low = SimpleLedActivator(3)
            low.setBLUE()
            #low.default_led()
            return
        else:
            return
        
    def getActuator_obj(self):
        return self.actuator_status
