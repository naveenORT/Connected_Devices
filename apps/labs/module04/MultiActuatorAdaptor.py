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


class MultiActuatorAdaptor():
    
    
    def __init__(self):
        logging.info("Going to Performing Actuation")     
        #self.temp_act()
        self.humidity_api_act()
        self.humidity_i2c_act()
    def temp_act(self):    
        if  (data_object.getActuationStae() is True):
                temp_actuator_status = ActuatorData()
                temp_actuator_status.addData("temp_inbound", data_object.getcurvalue(), "Temp Sensor")  # logging actuator data
                api_message = SimpleLedActivator(10)
                api_message.show_api_LED(data_object.getcurvalue())
                return        
        
    def humidity_api_act(self):    
        if (humidity_data_object.getActuationStae() is True):
                humidity_actuator_status = ActuatorData()
                humidity_actuator_status.addData("api_inbound", humidity_data_object.getcurvalue(), "Humidity_API")  # logging actuator data
                api_message = SimpleLedActivator(10)
                api_message.show_api_LED(humidity_data_object.getcurvalue())
                return
    
    def humidity_i2c_act(self):    
        if  (i2c_data_object.getActuationStae() is True):
                i2c_actuator_status = ActuatorData()
                i2c_actuator_status.addData("i2c_inbound", i2c_data_object.getcurvalue(), "Humidity_I2C")  # logging actuator data
                i2c_message = SimpleLedActivator()
                i2c_message.show_i2c_LED(i2c_data_object.getcurvalue())
                return
            