'''
Created on Apr 8, 2020


@author: Naveen Rajendran
'''
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
from labs.module09.OPC_Client_Rpi import OPC_Client_Rpi
from labs.module09.SensorDataManager import SensorDataManager
import time
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


def main():
    SensorData_Object = ArduinoDataReceiver()
    SensorData_Object.start()
    time.sleep(2)
    opc = OPC_Client_Rpi()
    opc.start()
    sdm = SensorDataManager()
    sdm.start()
    
main()
