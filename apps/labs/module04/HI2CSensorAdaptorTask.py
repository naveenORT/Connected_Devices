'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
import threading
import time
import smbus2
import numpy as np
import logging


class HI2CSensorAdaptorTask(threading.Thread):
    """      
    * Constructor function which sets daemon of TempSensorAdaptorTask thread to true 
    """       
    i2c_data_object = SensorData()
    i2cBus = smbus2.SMBus(1)    
    pressAddr = 0x5C  # address for pressure sensor
    humidAddr = 0x5F  # address for humidity sensor
    
    def __init__(self, max_sample):
        threading.Thread.__init__(self)  # Invoking Thread Function
        HI2CSensorAdaptorTask.setDaemon(self, True)
        self.max_sample = max_sample
        self.initI2CBus()

    """      
    * This function uses sensehat function to extract temperature data and returns
    """       

    def getSensorData(self):
        
        H0_rh = np.uint16(self.i2cBus.read_byte_data(0x5f, 0x30) >> 1)
        H1_rh = np.uint16(self.i2cBus.read_byte_data(0x5f, 0x31) >> 1)
        
        lsb1 = self.i2cBus.read_byte_data(0x5f, 0x36)
        msb1 = self.i2cBus.read_byte_data(0x5f, 0x37)
        HO_T_OUT = np.int16((msb1 << 8) | lsb1)
    
        lsb2 = self.i2cBus.read_byte_data(0x5f, 0x3A)
        msb2 = self.i2cBus.read_byte_data(0x5f, 0x3B)
        H1_T_OUT = np.int16((msb2 << 8) | lsb2)  
        
        lsb = self.i2cBus.read_byte_data(0x5f, 0x28)
        msb = self.i2cBus.read_byte_data(0x5f, 0x29)
        H_T_OUT = np.int16((msb << 8) | lsb)
          
        RH = ((H1_rh - H0_rh) * (H_T_OUT - HO_T_OUT) / (H1_T_OUT - HO_T_OUT)) + H0_rh
        
        return RH

    def initI2CBus(self):
        logging.info("Initializing I2C bus and enabling I2C addresses...")
        self.i2cBus.write_byte_data(self.pressAddr, 0, 0)
        self.i2cBus.write_byte_data(self.humidAddr, 0, 0)

    """      
    * Runnable thread function which uses function of SensorData to record values
    """       

    def displayHumidityData(self):
        q = self.i2cBus.read_byte_data(0x5f, 0x28)
        w = self.i2cBus.read_byte_data(0x5f, 0x29)
        e = self.i2cBus.read_byte_data(0x5f, 0x36)
        r = self.i2cBus.read_byte_data(0x5f, 0x37)
        t = self.i2cBus.read_byte_data(0x5f, 0x30)
        y = self.i2cBus.read_byte_data(0x5f, 0x31)
        u = self.i2cBus.read_byte_data(0x5f, 0x3A)
        i = self.i2cBus.read_byte_data(0x5f, 0x3B)
        o = [q, w, e, r, t, y, u, i]
        print("HUMIDITY BLOCK DATA ", o)
    
    
    def run(self):    
        while HI2CSensorAdaptorTask.isDaemon(self):    
            i2c_humidity = self.getSensorData()
            self.i2c_data_object.addValue(i2c_humidity)  # Logging sensor data
            print(i2c_humidity)
            self.displayHumidityData()
            time.sleep(4)
            self.max_sample -= 1                    
            if self.max_sample == 0:
                return
    
