'''
Created on Apr 15, 2020
@author: Naveen Rajendran
'''
import paho.mqtt.client as mqttClient
import time
import json
import ssl
from labs.common.DataUtil import DataUtil
from labs.common.ConfigUtil import ConfigUtil
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.ArduinoDataReceiver import DeviceData_Object
import threading
from labs.module09.SensorDataManager import logging

mqtt_client = mqttClient.Client()
connected = False  
convert_json = DataUtil()


class UbidotsCloudConnector(threading.Thread):    
    
    def __init__(self):        
        threading.Thread.__init__(self)
        self.load_prop = ConfigUtil(r"/home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props")
     
        self.BROKER_ENDPOINT = self.load_prop.getValues('ubidots.cloud', 'host')
        self.TLS_PORT = int(self.load_prop.getValues('ubidots.cloud', 'port'))
        self.MQTT_USERNAME = self.load_prop.getValues('ubidots.cloud', 'authToken')  
        self.MQTT_PASSWORD = ""  
        self.TOPIC = '/v1.6/devices/'
        self.DEVICE_LABEL = 'substation-gateway'
        self.TLS_CERT_PATH = self.load_prop.getValues('ubidots.cloud', 'certFile')  
        logging.info("Configuring & Setting Up Cloud Connection Properties")
        self.connect(mqtt_client, self.MQTT_USERNAME, self.MQTT_PASSWORD, self.BROKER_ENDPOINT, self.TLS_PORT)
    
    def connect(self, mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
        
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.tls_set(ca_certs=self.TLS_CERT_PATH, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()
    
         
            
    def run(self): 
        while(1):
            topic = "{}{}".format(self.TOPIC, self.DEVICE_LABEL)
            sensor_payload = convert_json.sensordatatojson(SensorData_Object)
            device_payload = convert_json.sensordatatojson(DeviceData_Object)
            print(sensor_payload + "\n" + device_payload)
        
            self.publish(mqtt_client, topic, sensor_payload)
            self.publish(mqtt_client, topic, device_payload)
            
            time.sleep(5)
        
    def publish(self, mqtt_client, topic, payload): 
        try:
            mqtt_client.publish(topic, payload)
            logging.info("Data Published")
        except Exception as e:
            print("[ERROR] Could not publish data, error: {}".format(e))
