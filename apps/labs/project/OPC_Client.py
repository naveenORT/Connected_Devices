'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import threading
import time
from labs.project.ArduinoDataReceiver import ArduinoDataReceiver

class OPC_Client(threading.Thread):
    
    
    def __init__(self):
        threading.Thread.__init__()
        
        
    def run(self):   
        SensorData = ArduinoDataReceiver()
        SensorData.start()