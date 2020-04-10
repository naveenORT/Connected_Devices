'''
Created on Apr 2, 2020
@author: Naveen Rajendran
'''
import threading
import time
from opcua import Client
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.SensorDataManager import logging


class OPC_Client_Rpi(threading.Thread):
        
    def __init__(self):
        threading.Thread.__init__(self)
        self.opc_client = Client("opc.tcp://10.0.0.57:4048")
        self.opc_client.connect()
        self.initiate_nodes()
     
    def initiate_nodes(self):    
        
        self.temp_value = self.opc_client.get_node('ns=2; s="Cabin_Temperature"')
        self.hum_value = self.opc_client.get_node('ns=2; s="Room_Humidity"')
        self.flux_value = self.opc_client.get_node('ns=2; s="Magnetic_Flux"')
        self.corona_level = self.opc_client.get_node('ns=3; s="Salt_Level"')
        self.resistance = self.opc_client.get_node('ns=3; s="Rod_Resistence"')
    
    def run(self):
        time.sleep(5)
        while(1):
            time.sleep(0.5)
            temperature = SensorData_Object.getTemperature()
            self.temp_value.set_value(temperature)        
        
            humidity = SensorData_Object.getHumidity()
            self.hum_value.set_value(humidity)
        
            flux = SensorData_Object.getMagFlux()
            self.flux_value.set_value(flux)
            
            corona_level = SensorData_Object.getCorona()
            self.corona_level.set_value(corona_level) 
            
            Resistence = SensorData_Object.getResistence()
            self.resistance.set_value(Resistence)
            
            logging.getLogger('Main').info("All Data Published to OPC Server")