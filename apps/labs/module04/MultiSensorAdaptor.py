'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module04.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module04.TempSensorAdaptorTask import data_object  
from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
import logging
import threading


class MultiSensorAdaptor(threading.Thread):
   
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("started logging")
        temp_sensor_object = TempSensorAdaptorTask(20)
        temp_sensor_object.start()  # Starting Threaded Class Object
        humi_sensorAPI_object = HumiditySensorAdaptorTask(20)
        humi_sensorAPI_object.start()  # Starting Threaded Class Object
        #self.humi_sensori2c_object = HI2CSensorAdaptorTask(20)
        #self.humi_sensori2c_object.start()  # Starting Threaded Class Object
    
    def getSensorobj(self):
        return self.temp_sensor_object


