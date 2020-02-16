'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
import random

'''
***********************************Module Description********************************************************************************
* In this module sense hat library function is imported for sensing temperature prevailing in external environment
* It is a threaded class which gets instantiated whenever the instance of TempSensorAdaptorClass gets created
* Functions get_temperature_from_pressure & get_temperature_from_humidity, helps to obtain read outs from GPIO pins
* Readed temperature value is passed on to instance of SensorData class & temperature values from sense hat are stored 
*************************************************************************************************************************************
'''

humidity_data_object = SensorData()  # class object


class HumiditySensorAdaptorTask(threading.Thread):
    '''      
    * Constructor function which sets daemon of TempSensorAdaptorTask thread to true 
    '''       
    
    humidity_data_object.set_sensor_name("Humidity_API")
    sense_hat = SenseHat()  # class object

    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        HumiditySensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    '''      
    * This function uses sensehat function to extract temperature data and returns
    '''       

    def getSensorData(self):
        t1 = self.sense_hat.get_humidity()  # Obtain temperature from humidity
        return t1 
    
    '''      
    * Runnable thread function which uses function of SensorData to record values
    '''       

    def run(self):    
        while HumiditySensorAdaptorTask.isDaemon(self):    
            time.sleep(4)
            api_humidity = self.getSensorData()
            print ("Humidity Value from sense hat API:" , api_humidity) 
            humidity_data_object.addValue(api_humidity)  # Logging sensor data
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return
    
    def getApiSensorDataObject(self):               
        return humidity_data_object
