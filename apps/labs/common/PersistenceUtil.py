'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
from labs.common.DataUtil import DataUtil
import redis
import logging
from labs.common.ActuatorData import ActuatorData
from labs.common.SensorData import SensorData
from labs.common.ActuatorDataListener import ActuatorDataListener


class PersistenceUtil():
    
    util = DataUtil()
    
    def __init__(self, input_obj):
        
        if (isinstance(input_obj, SensorData)):
            sd = self.util.sensordatatojson(input_obj) 
            self.writeSensorDatatoDbms(sd)
            
        elif (isinstance(input_obj, ActuatorData)):
            ad = self.util.actuatordatatojson(input_obj)
            self.writeActuatorDatatoDbms(ad)
 
    def writeActuatorDatatoDbms(self, json_actuator_data):    
        self.redis_actuator_data = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_actuator_data.set('ActuatorData', json_actuator_data)
        print(self.redis_actuator_data.get('ActuatorData'))
        self.registerActuatorDataListener()
    
    def writeSensorDatatoDbms(self, json_sensor_data):    
        self.redis_sensor_data = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.redis_sensor_data.set('SensorData', json_sensor_data)
        print(self.redis_sensor_data.get('SensorData'))
    
    def registerActuatorDataListener(self):
        self.x = ActuatorDataListener(self.redis_actuator_data)
    
    def registerSensorDataListener(self):
        return
    
    def get_Register_Actuator_Data(self):
        return self.x
    
    def get_Register_Sensor_Data(self):
        return 