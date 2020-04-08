'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import logging
from labs.Project_Final.ArduinoDataReceiver import ArduinoDataReceiver
from labs.Project_Final.OPC_Client_Rpi import OPC_Client_Rpi
import threading
SensorData_Object = ArduinoDataReceiver()


class SensorHandlerApp(threading.Thread):
   
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    
    def __init__(self):        
        threading.Thread.__init__()
        logging.info("Started")
    
    def run(self):
        SensorData_Object.start()
        opc = OPC_Client_Rpi()
        opc.start()
        
