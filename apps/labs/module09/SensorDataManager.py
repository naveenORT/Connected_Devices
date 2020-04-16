'''
Created on Apr 9, 2020

@author: Naveen Rajendran
'''
import threading
import time
import logging
from lib_nrf24 import NRF24
import spidev
import RPi.GPIO as GPIO
from labs.module09.ArduinoDataReceiver import SensorData_Object
from labs.module09.SmtpClientConnector import smtpconnect
from labs.module09.UbidotsCloudConnector import act_obj
SMTP = smtpconnect()
logging = logging.getLogger("Main")
radio = NRF24(GPIO, spidev.SpiDev())
        

class SensorDataManager(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def send_notification(self):
        
        if (SensorData_Object.getHumidity() > 50):
            
            logging.info("\n" + "Humidity Exceeded By" + str(SensorData_Object.getHumidity() - 50) + "Units" )
            data = "Excess Humidity Value Detected @ Site" + str(SensorData_Object.getHumidity())
            SMTP.publishMessage("Excess Humidity Detected", data)
    
        if (SensorData_Object.getResistence() > 110):
            
            logging.info("\n" + "Resistence Exceeded By" + str(SensorData_Object.getResistence() - 110) + "Units" )
            data = "Excess Resistance Value Detected @ Site" + str (SensorData_Object.getResistence())
            SMTP.publishMessage("Excess Resistance Detected", data)
    
        if (SensorData_Object.getCorona() > 50):
            
            logging.info("\n" + "Corona-Level Exceeded By" + str(SensorData_Object.getCorona() - 50) +"Units")
            data = "Excess Corona_level Value Detected @ Site" + str (SensorData_Object.getCorona())
            SMTP.publishMessage("Excess Corona Detected", data)
    
        if (SensorData_Object.getTemperature() > 40):
            
            logging.info("\n" + "Temperature Level Exceeded By" + str(SensorData_Object.getTemperature() - 40) +"Units" ) 
            data = "Excess Temperartue Value Detected @ Site" + str(SensorData_Object.getTemperature())
            SMTP.publishMessage("Excess Temperature Detected", data)
    
        if (SensorData_Object.getMagFlux() > 50):
            
            logging.info("\n" + "Temperature Level Exceeded By" + str(SensorData_Object.getMagFlux() - 50) +"Units" ) 
            data = "Excess Induction Value Detected @ Site" + str(SensorData_Object.getTemperature())
            SMTP.publishMessage("Excess Magnetic Flux Detected", data)
    
    def perform_actuation(self):
        
        print(act_obj.getRelay())
        pipe = [0xD2, 0XD2, 0XD2, 0XD2, 0XD2]
        radio.openWritingPipe(pipe)
        
        if (act_obj.getRelay() != None):
            logging.info("\n" + "Actuator Data Received From cloud")
            
            message = list("H")
            
            while len(message) < 32:
                message.append(0)
            
            if (act_obj.getRelay() is True):
                radio.write(message)
                logging.info("Safety Relay Activated!!")
    
            elif (act_obj.getRelay() is False):
                message = 'L'
                radio.write(message)
                logging.info("Safety Relay Deactivated")
        
        else:
            logging.info("Actuation Not Required")
            return
    
    def enableRadio(self):
        pipe = [0xD2, 0XD2, 0XD2, 0XD2, 0XD2]
        radio.begin(0, 17)        
        radio.setPayloadSize(32)
        radio.setChannel(0x76)
        radio.setDataRate(NRF24.BR_1MBPS)
        radio.setPALevel(NRF24.PA_MIN)
        radio.setAutoAck(True)
        radio.enableDynamicPayloads()
        radio.enableAckPayload()
        radio.openWritingPipe(pipe)
        
    def run(self):
        #self.enableRadio()
        while(1):
            self.send_notification()
            #self.perform_actuation()
            time.sleep(10)
