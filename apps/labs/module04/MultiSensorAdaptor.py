'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module04.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module04.TempSensorAdaptorTask import data_object  
from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
# from labs.module04.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
import logging
import threading
import time


class MultiSensorAdaptor(threading.Thread):
   
    def __init__(self):
        threading.Thread.__init__(self)
        MultiSensorAdaptor.setDaemon(self, True)
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("started logging")
    
    def run(self):    
         
        temp_sensor_object = TempSensorAdaptorTask(20)
        temp_sensor_object.start()  # Starting Threaded Class Object
        humi_sensorAPI_object = HumiditySensorAdaptorTask(20)
        humi_sensorAPI_object.start()  # Starting Threaded Class Object
        # humi_sensori2c_object = HI2CSensorAdaptorTask(20)
        # humi_sensori2c_object.start()  # Starting Threaded Class Object
        time.sleep(10)

    def getSensorobj(self):
        return self.temp_sensor_object

