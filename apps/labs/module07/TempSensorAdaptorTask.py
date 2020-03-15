'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time

from labs.common.DataUtil import DataUtil
from labs.module07.CoAPClientConnector import CoAPClientConnector
data_object = SensorData()  # class object
sense_hat = SenseHat()  # class object
coap = CoAPClientConnector()
du = DataUtil()
'''
* This class polls temperature sensor data from sense hat via its API  
'''


class TempSensorAdaptorTask(threading.Thread):
    '''      
    * Constructor function which sets daemon of TempSensorAdaptorTask thread to true 
    '''       
    data_object.set_sensor_name("Temperature Sensor")
    
    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        TempSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
    
    '''      
    * This function uses sensehat function to extract temperature data and returns
    '''       

    def getSensorData(self):
        t1 = sense_hat.get_temperature_from_humidity()  # Obtain temperature from humidity
        t2 = sense_hat.get_temperature_from_pressure()  # Obtain temperature from pressure
        c_temperature = ((t1 + t2)) / 2
        return  c_temperature  
    
    '''      
    * Runnable thread function which uses function of SensorData to record values
    '''       

    def run(self):    
        
        while TempSensorAdaptorTask.isDaemon(self):        
            time.sleep(5)
            environment_temperature = round(self.getSensorData(), 2)
            data_object.addValue(environment_temperature)  # Logging sensor data
            # sensor_obj = PersistenceUtil(data_object)       
            self.jsonobj = du.sensordatatojson(data_object)
            if (data_object.getsamplecount() == 1):  # POST SensorData when 1'st sample is generated
                coap.post_SensorData(self.jsonobj)
                self.max_sample -= 1
            if (data_object.getsamplecount() > 1):  # PUT SensorData when 2nd to 'N' sample is generated
                coap.put_SensorData(self.jsonobj)            
                self.max_sample -= 1
            if self.max_sample == 0:  # IF Sample = 20 Exit
                return 0
    
    def json_obj(self):     
        return self.jsonobj   
    
    def get_coap_client_obj(self):
        return self.coap