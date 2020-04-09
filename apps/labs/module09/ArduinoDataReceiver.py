import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import threading
from sense_hat import SenseHat
from labs.module09.SensorData import SensorData
from cmath import sqrt
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xC2, 0xC2, 0xC2, 0xC2, 0xC2], [0x01, 0x02, 0x03, 0x04, 0x05]]
SensorData_Object = SensorData()
sense = SenseHat()


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
        self.radio.flush_rx()
        while(1):
            self.receive_data_from_cabindevice()
            self.receive_data_from_elecrticpit()
            time.sleep(2)
    
    def receive_data_from_cabindevice(self):
        arduinoMessage = []
        self.radio.read(arduinoMessage, self.radio.getDynamicPayloadSize())
        
        if(arduinoMessage[0] == 1):
            # print("Received from Cabin Device: {}".format(arduinoMessage))
            
            print("\n")
            self.cabin_temperature = round(arduinoMessage[2] / 4, 2)  
            SensorData_Object.add_Temp_Value(sense.get_temperature())
            print("Cabin Temp:" + str(sense.get_temperature()))
            
            self.room_humidity = round(arduinoMessage[4] / 3, 2)
            SensorData_Object.add_Humi_Value(sense.get_humidity())
            print("Room Humidity:" + str(sense.get_humidity()))
            
            mag = sense.get_compass_raw()
            mag_x = round(mag["x"], 2)
            mag_y = round(mag["y"], 2)
            mag_z = round(mag["z"], 2)
            mag_t = sqrt(abs(mag_x * mag_x + mag_y * mag_y + mag_z * mag_z))
            print("Magnetic Flux:" + str(abs(mag_t)))
            # self.magnetic_flux = arduinoMessage[6] / 10
            SensorData_Object.add_Mag_Value(abs(mag_t))
            
        else:
            return
    
    def receive_data_from_elecrticpit(self):    
        arduinoMessage = []
        self.radio.read(arduinoMessage, self.radio.getDynamicPayloadSize())
    
        if(arduinoMessage[0] == 2):
            # print("Received from Earthpit Device: {}".format(arduinoMessage)) 
            
            self.rod_resistence = arduinoMessage[2]  
            SensorData_Object.add_Res_Value(self.rod_resistence)
            print("Earthpit Resistence " + str(self.rod_resistence))
            
            self.rod_length = arduinoMessage[4]
            SensorData_Object.add_Cor_Value(self.rod_length)
            print("Ultrasound Level " + str(self.rod_length))
            print("\n")
        else:
            return
  
