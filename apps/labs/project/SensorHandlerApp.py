'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import time
import logging
from labs.project.ArduinoDataReceiver import ArduinoDataReceiver
from labs.project.OPC_Client_Rpi import OPC_Client_Rpi
import threading
SensorData_Object = ArduinoDataReceiver()


class SensorHandlerApp(threading.Thread):
   
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    
    def __init__(self):        
        threading.Thread.__init__()
        SensorData_Object.start()
        opc = OPC_Client_Rpi()
        opc.start()
        time.sleep(100)
    
