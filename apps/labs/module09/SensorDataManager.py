'''
Created on Apr 9, 2020

@author: Naveen Rajendran
'''
import threading
import time
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.SmtpClientConnector import smtpconnect

SMTP = smtpconnect()


class SensorDataManager(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def send_notification(self):
        
        if (SensorData_Object.getHumidity() > 50):
            data = "Excess Humidity Value Detected @ Site" + SensorData_Object.getHumidity()
            SMTP.publishMessage("Excess Temperature Detected", data)
    
        if (SensorData_Object.getResistence() > 110):
            data = "Excess Resistance Value Detected @ Site" + SensorData_Object.getResistence()
            SMTP.publishMessage("Excess Temperature Detected", data)
    
        if (SensorData_Object.getCorona() > 75):
            data = "Excess Corona_level Value Detected @ Site" + SensorData_Object.getCorona()
            SMTP.publishMessage("Excess Temperature Detected", data)
    
        if (SensorData_Object.getTemperature() > 25):
            data = "Excess Temperartue Value Detected @ Site" + SensorData_Object.getTemperature()
            SMTP.publishMessage("Excess Temperature Detected", data)
    
        if (SensorData_Object.getMagFlux() > 70):
            data = "Excess Induction Value Detected @ Site" + SensorData_Object.getTemperature()
            SMTP.publishMessage("Excess Temperature Detected", data)
    
    
    def run(self):
        time.sleep(10)
        while(1):
            self.send_notification()
            time.sleep(5)
