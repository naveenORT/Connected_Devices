'''
Created on Feb 29, 2020

@author: Naveen Rajendran
'''
import paho.mqtt.client as mqtt
import json
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil

# Define Variables
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 10
json_tool = DataUtil()

mqttc = mqtt.Client()


class MqttClientConnector():

    def __init__(self):
        mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)            
        print("MQTT SESSION ESTABLISHED")

    def publish_sensor_data(self, mqtt_topic, sensor_data):
        mqtt_message = json_tool.sensordatatojson(sensor_data)
        print(mqtt_message)
        mqttc.publish(mqtt_topic, mqtt_message)       
        
    def subscribe_actuator_data(self):
        mqttc.subscribe("ActuatorData")
    
    def on_received_actuator_data(self, client, userdata, msg):
        print(msg.topic)
        print(msg.payload)


def on_publish(mqttc, userdata, result):  # create function for callback
        print("Data Published \n")
        pass  

    
def on_message(client, userdata, message):
        print("message received " , str(message.payload.decode("utf-8")))
        print("message topic=", message.topic)
        print("message qos=", message.qos)
        print("message retain flag=", message.retain)

        
def on_connect(mqttc, userdata, flags, rc):
        print("connection ok \n")
        pass  


mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

