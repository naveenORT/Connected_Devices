'''
Created on Feb 20, 2020
@author: Naveen Rajendran
'''
import redis    
import logging


class ActuatorDataListener():
    
    def __init__(self, redis_input):
        self.on_Actuator_Message(redis_input)
    
    def on_Actuator_Message(self, in_redis_ActuatorData):    
        if(in_redis_ActuatorData.exists("ActuatorData")):
            print("LED actuation begins")
            return True
        else:
            print("Actuation signal not received")
            return False
    
