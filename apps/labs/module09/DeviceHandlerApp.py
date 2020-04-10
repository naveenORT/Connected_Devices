'''
Created on Apr 8, 2020
@author: Naveen Rajendran
'''
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
from labs.module09.OPC_Client_Rpi import OPC_Client_Rpi
from labs.module09.SensorDataManager import SensorDataManager
from labs.module09.DevicePerformanceMonitor import DevicePerformanceMonitor
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False



def main():
    
    SensorData_Object = ArduinoDataReceiver()
    SensorData_Object.start()
    
    time.sleep(2)
    
    opc = OPC_Client_Rpi()
    opc.start()
    
    sdm = SensorDataManager()
    sdm.start()
    
    dpm = DevicePerformanceMonitor()
    dpm.start()


main()
