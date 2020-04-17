import unittest
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
import time
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
from labs.module09.ActuatorAdaptor import ActuatorAdaptor

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = ArduinoDataReceiver()
		self.x.start()
	
	def testSensorData(self):
		time.sleep(5)
		exp1= self.x.getSensorData_object()
		self.assertTrue(isinstance(exp1.getCorona(),float))
	








if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()