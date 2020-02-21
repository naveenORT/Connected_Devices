'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
#from labs.common.DataUtil import DataUtil
from labs.common.PersistenceUtil import PersistenceUtil
'''
* In this module sense hat library function is imported for sensing humidity prevailing in external environment. 
* It is a threaded class which gets instantiated whenever the instance of MultiSensorAdaptorTask gets created. 
* Function getSensorData () helps to obtain read outs from GPIO pins using SenseHat library. 
* Sensed humidity value is passed on to instance of SensorData class & humidity values from sense hat are stored 
'''

humidity_data_object = SensorData()  # class object


class HumiditySensorAdaptorTask(threading.Thread):
    
    humidity_data_object.set_sensor_name("Humidity_APIs")
    sense_hat = SenseHat()  # class object
    
    '''      
    * Constructor function which sets daemon of HumiditySensorAdaptorTask thread to true 
    '''       

    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        HumiditySensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    '''      
    * This function uses sensehat function to extract temperature data and returns
      Output: Relative Humidity(float)
    '''       

    def getSensorData(self):
        t1 = self.sense_hat.get_humidity()  # Obtain temperature from humidity
        return t1 
    
    '''      
    * Runnable thread function which uses function of SensorData to record values
    '''       

    def run(self):
        time.sleep(0.5)    
        while HumiditySensorAdaptorTask.isDaemon(self):    
            time.sleep(6.5)
            api_humidity = self.getSensorData()
            print ("Humidity Value from sense hat API:" , api_humidity)
            humidity_data_object.addValue(api_humidity)  # Logging sensor data
            obj = PersistenceUtil(humidity_data_object)
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return

    '''
    * Standard getter function for humidit_data_object
      Output : humidity_data_object(SensorData)
    '''

    def getApiSensorDataObject(self):               
        return humidity_data_object
