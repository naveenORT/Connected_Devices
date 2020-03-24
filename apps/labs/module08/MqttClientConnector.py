'''
Created on Mar 19, 2020
@author: Naveen Rajendran
'''

import paho.mqtt.client as mqtt
import logging
import ssl
from labs.common.DataUtil import DataUtil
import json
from labs.module06.MqttClientConnector import on_publish
# Define Variables
json_tool = DataUtil()
mqttc = mqtt.Client()
act_data = ''
flag = False
'''
* This class is for the purpose of establishing connection between MQTT client & Broker
'''


class MqttClientConnector():
    '''
    * Constructor function establishes MQTT connection using predefined port no & IP address given by user
    '''
    
    def __init__(self, MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL, TSL_SEC, CERT_PATH, USER_NAME, PASSWORD):
       
        if (TSL_SEC == True):
            
            mqttc.tls_set(ca_certs=CERT_PATH, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
            mqttc.username_pw_set(USER_NAME, PASSWORD)
            mqttc.tls_insecure_set(False)
            mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
            mqttc.loop_start()
            
        else:
            mqttc.on_connect = on_connect
            mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)                    
            mqttc.loop_start()
            
    '''
    * Publish SensorData object in json format to GatewayHandlerApp using MQTT 
    * Input: mqtt-topic(String) & SensorData (Object)
    '''
        
    def publish_sensor_data(self, mqtt_topic, sensor_data):
        mqttc.on_publish = on_publish
        mqtt_message = json_tool.sensordatatojson(sensor_data)
        # print(mqtt_message)
        mqttc.publish(mqtt_topic, mqtt_message, 0)
        
    '''
    * public function for Subscribing to actuator_data
    '''

    def subscribe_actuator_data(self):
        mqttc.subscribe("ActuatorData")
        logging.getLogger().info("Subscribed to ActuatorData \n")
        mqttc.on_message = on_message
  
    def get_act_data(self):
        temp_data = json.loads(act_data)
        actuator_setpoint = temp_data["value"]
        return float(actuator_setpoint)
   
    def getflag(self):
        return flag 

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
    flag = True
