'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
import redis    
import logging
import json
from labs.common.DataUtil import DataUtil
from labs.module05.TempSensorAdaptorTask import data_object
from labs.common.AData import AData
import threading
import time


class ActuatorDataListener(threading.Thread):
    
    redis_server = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    util = DataUtil()
    actuation_counter = 1
    
    def __init__(self):
        threading.Thread.__init__(self)
      
    def on_Actuator_Message(self):    
         
        if(self.redis_server.exists(str(self.actuation_counter))):
            print("Above threshold ........LED actuation begins")
            self.x = self.redis_server.get(str(self.actuation_counter))
            self.y = self.util.jsonToActuatorData(self.x)
            self.actuation_counter = self.actuation_counter + 1
            return True

    def run(self):
        while(True):
            self.on_Actuator_Message()
            time.sleep(6.5)

    def get_alo_object(self):
        return self.y

    def get_x_jsonactdata(self):
        return self.x