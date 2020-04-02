import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import threading
import logging
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xC2, 0xC2, 0xC2, 0xC2, 0xC2], [0x01, 0x02, 0x03, 0x04, 0x05]]

    
class ArduinoDataReceiver(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__(self)
        self.radio = NRF24(GPIO, spidev.SpiDev())
        self.radio.begin(0, 17)
        
        self.radio.setPayloadSize(32)
        self.radio.setChannel(0x76)
        self.radio.setDataRate(NRF24.BR_1MBPS)
        self.radio.setPALevel(NRF24.PA_MIN)
        
        self.radio.setAutoAck(True)
        self.radio.enableDynamicPayloads()
        self.radio.enableAckPayload()
        
        self.radio.openReadingPipe(0, pipes[1])
        self.radio.openReadingPipe(1, pipes[2])
        self.radio.startListening()
    
    def run(self):
        while(1):
            self.receive_data_from_field()
            time.sleep(3)
    
    def receive_data_from_field(self):
        arduinoMessage = []
        self.radio.read(arduinoMessage, self.radio.getDynamicPayloadSize())
        
        if(arduinoMessage[0] == 1):
            print("Received from Cabin Device: {}".format(arduinoMessage))
            self.cabin_temperature = arduinoMessage[2]/4  
            logging.info("Cabin Temp:" + str(self.cabin_temperature))
            self.room_humidity = arduinoMessage[4]/3
            logging.info("Room Humidity:" + str(self.room_humidity))
            self.magnetic_flux = arduinoMessage[6]/1000
            logging.info("Magnetic Flux:" + str(self.magnetic_flux))
     
        if(arduinoMessage[0] == 2):
            print("Received from Earthpit Device: {}".format(arduinoMessage)) 
            self.rod_resistence = arduinoMessage[2]  
            logging.info("Earthpit Resistence " + str(self.rod_resistence))
            
            self.rod_length = arduinoMessage[4]
            logging.info("Salt Level " + str(self.rod_length))

    def getCabin_Temp(self):
        return self.cabin_temperature
    
    def getRoom_Humidity(self):
        return self.room_humidity
    
    def getMagnetic_flux(self):
        return self.magnetic_flux
    
    def getRod_Resistence(self):
        return self.rod_resistence
    
    def getRod_Length(self):
        return self.rod_length
