'''
Created on Apr 15, 2020
@author: Naveen Rajendran
'''
import paho.mqtt.client as mqttClient
import time
import ssl
from labs.common.DataUtil import DataUtil
from labs.common.ConfigUtil import ConfigUtil
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.ArduinoDataReceiver import DeviceData_Object
import threading
from labs.module09.SensorDataManager import logging
#from labs.module09.ActuatorAdaptor import ActuatorAdaptor

mqtt_client = mqttClient.Client()
connected = False  
convert_json = DataUtil()
flag = False


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
        mqtt_client.on_connect = on_connect

    def run(self): 
        while(1):
            topic = "{}{}".format(self.TOPIC, self.DEVICE_LABEL)
            sensor_payload = convert_json.sensordatatojson(SensorData_Object)
            device_payload = convert_json.sensordatatojson(DeviceData_Object)
            print(sensor_payload + "\n" + device_payload)
            self.publish(mqtt_client, topic, sensor_payload)
            self.publish(mqtt_client, topic, device_payload)
            mqtt_client.on_publish = on_publish

            mqtt_client.subscribe("/v1.6/devices/substation-gateway/relay_status")
            mqtt_client.on_message = on_message
            time.sleep(5)
        
    def publish(self, mqtt_client, topic, payload): 
        try:
            mqtt_client.publish(topic, payload)
            logging.info("Data Published")
        except Exception as e:
            print("[ERROR] Could not publish data, error: {}".format(e))

'''
* MQTT Callback function on connection establishment
'''


def on_connect(mqttc, userdata, flags, rc):
    if rc == 0:
        logging.getLogger().info("Connected to MQTT Broker Successfully CONNACK Received")
    else:
        logging.getLogger().info("Bad connection - MQTT Broker Not Running")
'''
* MQTT Callback function on publishing json data to MQTT Broker
'''    


def on_publish(mqttc, userdata, result):  # create function for callback
    logging.getLogger().info("Data Published to IoT Gateway App \n")

'''
* MQTT Callback function on receiving json ActuatorData via mqtt
'''    


def on_message(mqttc, userdata, message):
    global act_data
    global flag
    act_data = str(message.payload.decode("utf-8"))
    """
    if(act_data == "1"):
        ActuatorAdaptor.setRelay(True)
    else:
        ActuatorAdaptor.setRelay(False)
    flag = True
    """

mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.on_message = on_message
