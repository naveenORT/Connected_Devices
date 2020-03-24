'''
Created on Mar 22, 2020
@author: Naveen Rajendran
'''
from labs.module08.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module08.TempSensorAdaptorTask import data_object  
# from labs.module05.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
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
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.info("Sensor_Logging_Started!!!")
        
    '''
    * Runnable function which starts two seperate threads for polling humidity data via SenseHat api & i2c bus
    '''
    
    def run(self):    
        self.temp_sensor_object = TempSensorAdaptorTask(100)
        self.temp_sensor_object.start()  # Starting Threaded Class Object
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
                                            
