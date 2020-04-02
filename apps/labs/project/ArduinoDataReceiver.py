import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import threading
import logging
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xC2, 0xC2, 0xC2, 0xC2, 0xC2], [0x01, 0x02, 0x03, 0x04, 0x05]]
arduinoMessage = []

    
class ArduinoDataReceiver(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__()
        radio = NRF24(GPIO, spidev.SpiDev())
        radio.begin(0, 17)
        
        radio.setPayloadSize(32)
        radio.setChannel(0x76)
        radio.setDataRate(NRF24.BR_1MBPS)
        radio.setPALevel(NRF24.PA_MIN)
        
        radio.setAutoAck(True)
        radio.enableDynamicPayloads()
        radio.enableAckPayload()
        
        radio.openReadingPipe(0, pipes[1])
        radio.openReadingPipe(1, pipes[2])
        radio.printDetails()
        radio.startListening()
    
    def run(self):
        self.receive_data_from_field()
        time.sleep(2)
    
    def receive_data_from_field(self):
        self.radio.read(arduinoMessage, self.radio.getDynamicPayloadSize())
        if(arduinoMessage[0] == 1):
            print("Received from Cabin Device: {}".format(arduinoMessage))
            self.cabin_temperature = arduinoMessage[2]  
            logging.info("Cabin Temp:" + str(self.cabin_temperature))
            self.room_humidity = arduinoMessage[4]
            logging.info("Room Humidity:" + str(self.room_humidity))
            self.magnetic_flux = arduinoMessage[6]
            logging.info("Magnetic Flux:" + str(self.magnetic_flux))
     
        if(arduinoMessage[0] == 2):
            print("Received from Earthpit Device: {}".format(arduinoMessage)) 
            self.rod_resistence = arduinoMessage[2]  
            logging.info("Earthpit Resistence" + str(self.rod_resistence))
            
            self.rod_length = arduinoMessage[4]
            logging.info("Earthpit Resistence" + str(self.rod_length))

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
