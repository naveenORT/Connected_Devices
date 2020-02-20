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
            sd = self.util.sensordatatojson(input_obj) 
            self.writeSensorDatatoDbms(sd)
        elif (isinstance(input_obj, ActuatorData)):
            ad = self.util.actuatordatatojson(input_obj)
            self.writeActuatorDatatoDbms(sd)
 
    def writeActuatorDatatoDbms(self, json_actuator_data):    
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        r.set('ActuatorData', json_actuator_data)
    
    def writeSensorDatatoDbms(self, json_sensor_data):    
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        r.set('SensorData', json_sensor_data)
        print(r.get('SensorData'))
