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


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    log = logging.getLogger("Main")
    log.info(".started logging.")

    SensorData_Object = ArduinoDataReceiver()
    SensorData_Object.start()
    
    time.sleep(2)
    
    opc = OPC_Client_Rpi()
    opc.start()
    
 #   sdm = SensorDataManager()
 #   sdm.start()
    
 #   dpm = DevicePerformanceMonitor()
 #   dpm.start()


main()
