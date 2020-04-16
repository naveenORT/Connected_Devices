import logging
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import threading
from sense_hat import SenseHat
from labs.module09.SensorData import SensorData
from labs.module09.DeviceData import DeviceData
from cmath import sqrt
#from labs.module09.UbidotsCloudConnector import act_obj
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xC2, 0xC2, 0xC2, 0xC2, 0xC2], [0x01, 0x02, 0x03, 0x04, 0x05], [0xD2, 0XD2, 0XD2, 0XD2, 0XD2]]
SensorData_Object = SensorData()
DeviceData_Object = DeviceData()
sense = SenseHat()
radio = NRF24(GPIO, spidev.SpiDev())
       

class ArduinoDataReceiver(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
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
        radio.openWritingPipe(pipes[2])
        radio.startListening()
        
    def run(self):
        radio.flush_rx()        
        self.receive_data_from_cabindevice()
        self.receive_data_from_elecrticpit()
     
    def receive_data_from_cabindevice(self):
        while(1):
            arduinoMessage = []
            radio.read(arduinoMessage, radio.getDynamicPayloadSize())
            print(arduinoMessage)
            
            if(arduinoMessage[0] == 1):
                # print("Received from Cabin Device: {}".format(arduinoMessage))
                DeviceData_Object.setArduino1_status(True)
                print("\n")
                self.cabin_temperature = round(arduinoMessage[2] / 4, 2)  
                SensorData_Object.add_Temp_Value(round(sense.get_temperature(), 2))
                logging.info("Cabin Temp:" + str(round(sense.get_temperature(), 2)))
                
                self.room_humidity = round(arduinoMessage[4] / 3, 2)
                SensorData_Object.add_Humi_Value(sense.get_humidity())
                logging.info("Room Humidity:" + str(sense.get_humidity()))
                
                mag = sense.get_compass_raw()
                mag_x = round(mag["x"], 2)
                mag_y = round(mag["y"], 2)
                mag_z = round(mag["z"], 2)
                mag_t = sqrt(abs(mag_x * mag_x + mag_y * mag_y + mag_z * mag_z))
                logging.info("Magnetic Flux:" + str(abs(mag_t)))
                # self.magnetic_flux = arduinoMessage[6] / 10
                SensorData_Object.add_Mag_Value(abs(mag_t))
                
            else:
                DeviceData_Object.setArduino1_status(False)
        
            time.sleep(1.5)
    
    def receive_data_from_elecrticpit(self):    
        while(1):
            arduinoMessage = []
            radio.read(arduinoMessage, radio.getDynamicPayloadSize())
            print(arduinoMessage)
            radio.flush_rx()
            
            if(arduinoMessage[0] == 2):
                # print("Received from Earthpit Device: {}".format(arduinoMessage)) 
                DeviceData_Object.setArduino2_status(True)
                self.rod_resistence = arduinoMessage[2]  
                SensorData_Object.add_Res_Value(self.rod_resistence)
                logging.info("Earthpit Resistence " + str(self.rod_resistence))
                
                self.rod_length = arduinoMessage[4]
                SensorData_Object.add_Cor_Value(self.rod_length)
                logging.info("Corona Level " + str(self.rod_length))
                logging.info("\n")
            else:
                DeviceData_Object.setArduino1_status(False)
                return
            
            time.sleep(2)