'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module05.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module05.TempSensorAdaptorTask import data_object  
from labs.module05.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
#from labs.module05.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
import logging
import threading
import time

'''
* This module helps to invoke two different threads, which obtains humidity data by different methods. 
* It starts HumiditySensorAdaptorTask(), which polls humidity data using sensehat api library & I2ChumiditySensorAdaptor which polls 
  humidity data by interacting directly with i2c bus on raspberry pi   
'''


class MultiSensorAdaptor(threading.Thread):
   
    '''
    * Constructor function which sets MultiSensorAdaptor as a daemon thread
    '''

    def __init__(self):
        threading.Thread.__init__(self)
        MultiSensorAdaptor.setDaemon(self, True)
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("started logging")
    
    '''
    * Runnable function which starts two seperate threads for polling humidity data via SenseHat api & i2c bus
    '''
    
    def run(self):    
        temp_sensor_object = TempSensorAdaptorTask(20)
        temp_sensor_object.start()  # Starting Threaded Class Object
        self.humi_sensorAPI_object = HumiditySensorAdaptorTask(20)
        self.humi_sensorAPI_object.start()  # Starting Threaded Class Object
        #self.humi_sensori2c_object = HI2CSensorAdaptorTask(20)
        #self.humi_sensori2c_object.start()  # Starting Threaded Class Object
        time.sleep(100)

    '''
    * Standard getter function for temp_sensor_object
      Output: temp_sensor_object(SensorData)   
    ''' 

    def getSensorobj(self):
        return self.temp_sensor_object

    '''
    * Standard getter function for humi_sensori2c_object
      Output: humi_sensori2c_object(SensorData)
    '''

    def geti2cobject(self): 
        return self.humi_sensori2c_object

    '''
    * Standard getter function for humi_sensorAPI_object
      Output: humi_sensorAPI_object(SensorData)  
    '''    

    def getAPIobject(self):
        return self.humi_sensorAPI_object
