'''
Created on Apr 10, 2020
@author: Naveen Rajendran
'''

import paho.mqtt.client as paho
from labs.module09.SensorData import SensorData
import json
import ssl
from time import sleep
from random import uniform
connflag = False


def on_connect(client, userdata, flags, rc):  
    global connflag
    print ("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc))

 
def on_message(client, userdata, msg): 
    print(msg.topic + " " + str(msg.payload))
 
 
mqttc = paho.Client() 
mqttc.on_connect = on_connect 
mqttc.on_message = on_message  

awshost = "a1ztbtn0iha3oc-ats.iot.us-west-2.amazonaws.com"  
awsport = 8883  
clientId = "Publisher"  
thingName = "Publisher" 
caPath = "root-ca-cert.pem" 
certPath = "707349cdf2.cert.pem"  
keyPath = "707349cdf2.private.key" 
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60) 

mqttc.loop_start()  
obj = SensorData() 
while 1 == 1:
    sleep(5)
    if connflag == True:
        value = uniform(20.0, 25.0) 
        obj.corona = round(value / 2, 2)
        obj.temperature = round(value / 3, 2)
        obj.humidity = round(value / 4, 2)
        obj.resistence = round(value, 2)
        obj.magflux = round(value * 0.5, 2)
        obj.device_id = 1001
        json_data = json.dumps(obj.__dict__)        
        mqttc.publish('update/environment/dht1', json_data, qos=1)  
        print("msg sent" + json_data)  
    else:
        print("waiting for connection...")                  
