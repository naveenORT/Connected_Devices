'''
Created on Mar 6, 2020
@author: Naveen Rajendran
'''
from coapthon.client.helperclient import HelperClient
from coapthon.client.coap import CoAP
import logging
CoAP_HOST = "127.0.0.1"
CoAP_PORT = 5683
path = "SensorData"
CoAP_Server = HelperClient(server=(CoAP_HOST, CoAP_PORT))  # Establishing Connection to CoAP server with given properties

'''
* Class module which connects to CoAP server & executes POST, DELETE, PUT & GET operations   
'''


class CoAPClientConnector:
        '''
        * Class Constructor Function  
        '''
        post_flag = False
        put_flag = False
        get_flag = False
        del_flag = False
        
        def _init_(self): 
            logging.info("python CoAP client started ")
         
        '''
        * Public function that posts SensorData in json format to CoAP server   
        * Input: path (URL)
        '''            

        def post_SensorData(self, input):
            CoAP_Server.post(path, input)
            self.set_post_flag(True)

        '''
        * Public function that deletes SensorData on CoAP server   
        * Input: input (Json formatted SensorData object)
        '''            

        def delete_SensorData(self):  
            CoAP_Server.delete(path)
            self.set_del_flag(True)

        '''
        * Public function which updates/puts SensorData URL on CoAP server   
        * Input: input (Json formatted SensorData object)
        '''

        def put_SensorData(self, input): 
            CoAP_Server.put(path, input)
            self.set_put_flag(True)

        '''
        * Public function to get ActuatorData in json format from CoAP server   
        * Output: Json formatted ActuatorData object
        '''            

        def get_ActuatorData(self):
            CoAP_Server.get("ActuatorData")
            self.set_get_flag(True)
            
        def set_post_flag(self, input):
            self.post_flag = input
        
        def set_put_flag(self, input):
            self.put_flag = input
            
        def set_del_flag(self, input):
            self.del_flag = input
            
        def set_get_flag(self, input):
            self.get_flag = input
            
        def get_post_flag(self):
            return self.post_flag
        
        def get_put_flag(self):
            return self.put_flag
        
        def get_del_flag(self):
            return self.del_flag
        
        def get_get_flag(self):
            return self.get_flag
