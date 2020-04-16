'''
Created on Apr 9, 2020

@author: Naveen Rajendran
'''
import threading
import time
import logging
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.SmtpClientConnector import smtpconnect

SMTP = smtpconnect()
logging = logging.getLogger("Main")

class SensorDataManager(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def send_notification(self):
        
        if (SensorData_Object.getHumidity() > 50):
            data = "Excess Humidity Value Detected @ Site" + str(SensorData_Object.getHumidity())
            SMTP.publishMessage("Excess Humidity Detected", data)
    
        if (SensorData_Object.getResistence() > 110):
            data = "Excess Resistance Value Detected @ Site" + str (SensorData_Object.getResistence())
            SMTP.publishMessage("Excess Resistance Detected", data)
    
        if (SensorData_Object.getCorona() > 50):
            data = "Excess Corona_level Value Detected @ Site" + str (SensorData_Object.getCorona())
            SMTP.publishMessage("Excess Corona Detected", data)
    
        if (SensorData_Object.getTemperature() > 40):
            data = "Excess Temperartue Value Detected @ Site" + str(SensorData_Object.getTemperature())
            SMTP.publishMessage("Excess Temperature Detected", data)
    
        if (SensorData_Object.getMagFlux() > 50):
            data = "Excess Induction Value Detected @ Site" + str(SensorData_Object.getTemperature())
            SMTP.publishMessage("Excess Magnetic Flux Detected", data)
    
    
    def run(self):
        time.sleep(10)
        while(1):
            self.send_notification()
            time.sleep(1)
