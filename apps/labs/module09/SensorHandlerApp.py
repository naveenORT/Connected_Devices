'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import logging
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
from labs.module09.OPC_Client_Rpi import OPC_Client_Rpi
import threading
import time


SensorData_Object = ArduinoDataReceiver()
    
class SensorHandlerApp(threading.Thread):
   
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    
    def __init__(self):        
        threading.Thread.__init__(self)
        logging.info("Started")
    
    def run(self):
        global SensorData_Object
        
        opc = OPC_Client_Rpi()
        SensorData_Object.start()
        time.sleep(5)
        opc.start()
        

