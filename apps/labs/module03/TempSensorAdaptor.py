'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module03.TempSensorAdaptorTask import data_object  
import logging
import threading
import time

class TempSensorAdaptor(threading.Thread):
   
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("started logging")
        threading.Thread.__init__(self)
        sensor_object = TempSensorAdaptorTask(20)
        sensor_object.start()                      #Starting Threaded Class Object
        while True:
            pass