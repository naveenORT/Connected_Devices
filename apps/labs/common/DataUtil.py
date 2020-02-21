'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
import json
import logging
import redis
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
import pickle


class DataUtil():
    
    def __init__(self):
        logging.info("Using Data Utilities")
        
    def jsontosensordata(self, json_SensorData):
        json_SensorData = json.loads(json_SensorData)
        s_object = SensorData(**json_SensorData)
        return s_object 

    def sensordatatojson(self, SensorData):    
        jsonSensor_Data = json.dumps(SensorData.__dict__)
        return jsonSensor_Data
    
    def writesensordatatofile(self, json_SensorData):
        with open('SensorData.txt', 'wb') as SensorData_file:
            pickle.dump(json_SensorData, SensorData_file)
    
    def jsontoactuatordata(self, json_ActuatorData): 
        json_ActuatorData = json.load(json_ActuatorData)
        a_object = ActuatorData(**json_ActuatorData)
        return a_object
        
    def actuatordatatojson(self, ActuatorData):
        jsonActuator_Data = json.dumps(ActuatorData.__dict__)
        return jsonActuator_Data
    
    def writeactuatordata(self, json_ActuatorData):            
        with open('ActuatorData.txt', 'wb') as ActuatorData_file:
            pickle.dump(json_ActuatorData, ActuatorData_file)
        
