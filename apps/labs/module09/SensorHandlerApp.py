'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import logging
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
from labs.module09.OPC_Client_Rpi import OPC_Client_Rpi
import threading
import time

class SensorHandlerApp(threading.Thread):
   
    def __init__(self):        
        threading.Thread.__init__(self)
        
    def run(self):
        SensorData_Object = ArduinoDataReceiver()
        SensorData_Object.start()
        time.sleep(2)
        opc = OPC_Client_Rpi()
        opc.start()
        

