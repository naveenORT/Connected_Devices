'''
Created on Apr 8, 2020
@author: Naveen Rajendran
'''
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
from labs.module09.OPC_Client_Rpi import OPC_Client_Rpi
from labs.module09.SensorDataManager import SensorDataManager
from labs.module09.DevicePerformanceMonitor import DevicePerformanceMonitor
from labs.module09.UbidotsCloudConnector import UbidotsCloudConnector        

import time

    
class GatewayHandlerApp():       
    SensorData_Object = ArduinoDataReceiver()  # Get Data from Constrained Device
    SensorData_Object.start()
    
    time.sleep(10)
    
    #OPC = OPC_Client_Rpi()  # Backup data at OPC_ Server
    #OPC.start()
    
    SDM = SensorDataManager()  # Publish SensorData to Ubidots Cloud & Trigger Notification
    SDM.start()
    
    DPM = DevicePerformanceMonitor()  # Compute Device Performance
    DPM.start()

    UCC = UbidotsCloudConnector()
    UCC.start()

    def getArduino_Receiver_Obj(self):
        return self.SensorData_Object
    
    def getOPC_Client_Rpi(self):
        return self.SensorData_Object
    
    def getSensorDataManager(self):
        return self.SDM

    def devicePerfMonit(self):
        return self.DPM
    
    def getUbidotsCloudConnector(self):
        return self.UCC

x = GatewayHandlerApp()    