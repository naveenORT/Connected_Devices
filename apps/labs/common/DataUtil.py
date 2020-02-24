'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
import json
import logging
import redis
from labs.common.ActuatorData import ActuatorData
from labs.common.AData import AData
import pickle


class DataUtil():
    
    def __init__(self):
        logging.info("Using Data Utilities")
        
    def jsonToActuatorData(self, jsonData):
        
        adDict = json.loads(jsonData)
        ad = AData()
        ad.sensor_name = adDict["sensor_name"]
        ad.input_command = adDict["input_command"]
        ad.current_actuator_status = adDict["current_actuator_status"]
        ad.sensor_value = adDict["sensor_value"]
        ad.actuation_state = adDict["actuation_state"]
        print(" decode [post] --> " + str(ad.sensor_name))
        print(" decode [post] --> " + str(ad.input_command))
        print(" decode [post] --> " + str(ad.current_actuator_status))
        print(" decode [post] --> " + str(ad.sensor_value))
        print(" decode [post] --> " + str(ad.actuation_state))
        
        return ad 

    def sensordatatojson(self, SensorData):    
        jsonSensor_Data = json.dumps(SensorData.__dict__)
        return jsonSensor_Data
    
    def writesensordatatofile(self, json_SensorData):
        with open('SensorData.txt', 'wb') as SensorData_file:
            pickle.dump(json_SensorData, SensorData_file)
        
    def actuatordatatojson(self, ActuatorData):
        jsonActuator_Data = json.dumps(ActuatorData.__dict__)
        return jsonActuator_Data
    
    def writeactuatordata(self, json_ActuatorData):            
        with open('ActuatorData.txt', 'wb') as ActuatorData_file:
            pickle.dump(json_ActuatorData, ActuatorData_file)
        
