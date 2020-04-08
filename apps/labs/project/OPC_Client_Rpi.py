'''
Created on Apr 2, 2020
@author: Naveen Rajendran
'''
import threading
from opcua import Client
from labs.project.SensorHandlerApp import SensorData

class OPC_Client_Rpi(threading.Thread):

        
    def __init__(self):
    
        self.opc_client = Client("opc.tcp://10.0.0.57:4048")
        self.opc_client.connect()
        self.initiate_nodes()
     
    def initiate_nodes(self):    
        
        self.temp_value = self.opc_client.get_node('ns=2; s="Cabin_Temperature"')
        self.hum_value =  self.opc_client.get_node('ns=2; s="Room_Humidity"')
        self.flux_value = self.opc_client.get_node('ns=2; s="Room_Humidity"')
        self.corona_level = self.opc_client.get_node('ns=3; s="Salt_Level"', "SaltLevel")
        self.resistance = self.opc_client.get_node('ns=3; s="Rod_Resistence"', "Resistance")
    
    def run(self):
        
        threading.Thread.__init__()    
        
        while(1):
            
            temperature = SensorData.getCabin_Temp()
            self.temp_value.set_value(temperature)        
        
            humidity = SensorData.getRoom_Humidity()
            self.hum_value.set_value(humidity)
        
            flux = SensorData.getMagnetic_flux()
            self.flux_value.set_value(flux)
            
            corona_level = SensorData.getRod_Length()
            self.corona_level.set_value(corona_level) 
            
            Resistence = SensorData.getRod_Resistence()
            self.resistance.set_value(Resistence)