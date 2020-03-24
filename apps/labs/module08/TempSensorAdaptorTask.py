'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
from labs.common.ConfigUtil import ConfigUtil
from labs.module08.MqttClientConnector import MqttClientConnector
import logging

data_object = SensorData()  # class object
sense_hat = SenseHat()  # class object
load_property = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props") 

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
        logging.getLogger().info("SensorData Creation Started")

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
        host = load_property.getValues("mqtt.gateway", "host")
        port = int(load_property.getValues("mqtt.gateway", "port"))
        cert_path = load_property.getValues("ubidots.cloud", "certFile")
        user_name = load_property.getValues("ubidots.cloud", "apiKey")
        password = load_property.getValues("ubidots.cloud", "authToken")
        mqttc = MqttClientConnector(host, port, 40, False, cert_path, user_name, password)

        while TempSensorAdaptorTask.isDaemon(self):        
            
            time.sleep(7)
            print("\n")
            environment_temperature = self.getSensorData()
            data_object.addValue(environment_temperature)  # Logging sensor data
            # sensor_obj = PersistenceUtil(data_object)       
            mqttc.publish_sensor_data("TempSensorData", data_object)
            mqttc.subscribe_actuator_data()
            time.sleep(5)
            if(mqttc.getflag()== True):
                print("<<<<<<<<<<-----------------Actuator Temperature arrived from Ubidots!", mqttc.get_act_data())
            else:
                continue
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return 0
    
