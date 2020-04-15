'''
Created on Apr 15, 2020
@author: Naveen Rajendran
'''
import paho.mqtt.client as mqttClient
import time
import json
import ssl
from labs.common.ConfigUtil import ConfigUtil
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.ArduinoDataReceiver import DeviceData_Object
import threading
from labs.module09.SensorDataManager import logging


class UbidotsCloudConnector(threading.Thread):    
    
    def __init__(self):        
        threading.Thread.__init__(self)
        self.load_prop = ConfigUtil(r"home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props")
        self.connected = False  
        self.BROKER_ENDPOINT = self.load_prop.getValues('ubidots.cloud', 'host')
        self.TLS_PORT = int(self.load_prop.getValues('ubidots.cloud', 'port'))
        self.MQTT_USERNAME = self.load_prop.getValues('ubidots.cloud', 'authToken')  
        self.MQTT_PASSWORD = ""  
        self.TOPIC = '/v1.6/devices/'
        self.DEVICE_LABEL = 'substation-gateway'
        self.TLS_CERT_PATH = self.load_prop.getValues('ubidots.cloud', 'certFile')  
        self.mqtt_client = mqttClient.Client() 
        logging.info("Configuring & Setting Up Cloud Connection Properties")
    
    def publish(self, mqtt_client, topic, payload): 
        try:
            mqtt_client.publish(topic, payload)
    
        except Exception as e:
            print("[ERROR] Could not publish data, error: {}".format(e))

    def connect(self, mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
        global connected

        if not connected:
            mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
            mqtt_client.on_connect = on_connect
            mqtt_client.on_publish = on_publish
            mqtt_client.tls_set(ca_certs=self.TLS_CERT_PATH, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
            mqtt_client.tls_insecure_set(False)
            mqtt_client.connect(broker_endpoint, port=port)
            mqtt_client.loop_start()
        
            attempts = 0
        
            while not connected and attempts < 5:  # Wait for connection
                print(connected)
                print("Attempting to connect...")
                time.sleep(1)
                attempts += 1
        
        if not connected:
            print("[ERROR] Could not connect to broker")
            return False
        
        return True

        def run(): 
            
            topic = "{}{}".format(self.TOPIC, self.DEVICE_LABEL)
            sensor_payload = json.dumps(SensorData_Object)
            device_payload = json.dumps(DeviceData_Object)
            print(sensor_payload + "\n" + device_payload)
            
            if not self.connect(mqtt_client, self.MQTT_USERNAME, self.MQTT_PASSWORD, self.BROKER_ENDPOINT, self.TLS_PORT):
                return False
            self.publish(mqtt_client, topic, sensor_payload)
            self.publish(mqtt_client, topic, device_payload)
            return True
            
            time.sleep(2)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")


def on_publish(client, userdata, result):
    print("Published!")
