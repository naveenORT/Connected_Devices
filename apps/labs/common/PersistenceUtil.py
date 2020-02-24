'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
from labs.common.DataUtil import DataUtil
import redis
import logging
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData


class PersistenceUtil():
    
    util = DataUtil()
    
    def __init__(self, input_obj):
        
        if (isinstance(input_obj, SensorData)):
            self.sdo = input_obj
            sd = self.util.sensordatatojson(self.sdo) 
            print(sd)
            self.writeSensorDatatoDbms(sd)
            
        elif (isinstance(input_obj, ActuatorData)):
            self.ado = input_obj
            ad = self.util.actuatordatatojson(self.ado)
            print(ad)
            self.writeActuatorDatatoDbms(ad)
 
    def writeActuatorDatatoDbms(self, json_actuator_data):    
        self.redis_actuator_data = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_actuator_data.set('ActuatorData', json_actuator_data)
     
    
    def writeSensorDatatoDbms(self, json_sensor_data):    
        self.redis_sensor_data = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_sensor_data.set('SensorData', json_sensor_data)
    
    