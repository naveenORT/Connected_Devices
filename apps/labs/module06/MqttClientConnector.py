'''
Created on Feb 29, 2020
@author: Naveen Rajendran
'''
import paho.mqtt.client as mqtt
import json
from labs.common.DataUtil import DataUtil

# Define Variables
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 40
json_tool = DataUtil()

mqttc = mqtt.Client()
'''
* This class is for the purpose of establishing connection between MQTT client & Broker
'''


class MqttClientConnector():
    '''
    * Constructor function establishes MQTT connection using predefined port no & IP address given by user
    '''

    def __init__(self):
        mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)                    
        print("MQTT SESSION ESTABLISHED")
        mqttc.loop_start()

    '''
    * Publish SensorData object in json format to GatewayHandlerApp using MQTT 
    * Input: mqtt-topic(String) & SensorData (Object)
    '''
        
    def publish_sensor_data(self, mqtt_topic, sensor_data):
        mqtt_message = json_tool.sensordatatojson(sensor_data)
        print(mqtt_message)
        mqttc.publish(mqtt_topic, mqtt_message, 2)

    '''
    * public function for Subscribing to actuator_data
    '''

    def subscribe_actuator_data(self):
        mqttc.subscribe("ActuatorData")

    def get_x(self):
        return self.publish_status

'''
* MQTT Callback function on connection establishment
'''


def on_connect():
        print("connection ok \n") 

'''
* MQTT Callback function on publishing json data to MQTT Broker
'''    


def on_publish(mqttc, userdata, result):  # create function for callback
        publish_status = True
        print("Data Published \n")
        return publish_status
'''
* MQTT Callback function on receiving json ActuatorData via mqtt
'''    


def on_message(mqttc, userdata, message):
        print("message received ", str(message.payload.decode("utf-8")))
        print("message topic=", message.topic)
        print("message qos=", message.qos)
        print("message retain flag=", message.retain)


mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message
