'''
Created on Apr 2, 2020
@author: Naveen Rajendran
'''
import threading
import time
from opcua import Client
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver

SensorData_Object = ArduinoDataReceiver()
class OPC_Client_Rpi(threading.Thread):
        
    def __init__(self):
        threading.Thread.__init__(self)
        self.opc_client = Client("opc.tcp://10.0.0.57:4048")
        self.opc_client.connect()
        self.initiate_nodes()
     
    def initiate_nodes(self):    
        
        self.temp_value = self.opc_client.get_node('ns=2; s="Cabin_Temperature"')
        self.hum_value = self.opc_client.get_node('ns=2; s="Room_Humidity"')
        self.flux_value = self.opc_client.get_node('ns=2; s="Room_Humidity"')
        self.corona_level = self.opc_client.get_node('ns=3; s="Salt_Level"')
        self.resistance = self.opc_client.get_node('ns=3; s="Rod_Resistence"')
    
    def run(self):
        
        
        while(1):
            time.sleep(0.5)
            temperature = SensorData_Object.getCabin_Temp()
            self.temp_value.set_value(temperature)        
        
            humidity = SensorData_Object.getRoom_Humidity()
            self.hum_value.set_value(humidity)
        
            flux = SensorData_Object.getMagnetic_flux()
            self.flux_value.set_value(flux)
            
            corona_level = SensorData_Object.getRod_Length()
            self.corona_level.set_value(corona_level) 
            
            Resistence = SensorData_Object.getRod_Resistence()
            self.resistance.set_value(Resistence)
