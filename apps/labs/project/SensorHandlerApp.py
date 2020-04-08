'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import logging
from labs.project.ArduinoDataReceiver import ArduinoDataReceiver
from labs.project.OPC_Client_Rpi import OPC_Client_Rpi

SensorData = ArduinoDataReceiver()
        
class SensorHandlerApp:
   
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    
    def __init__(self):        
        SensorData.start()
        opc = OPC_Client_Rpi()
        opc.start()
    
    
