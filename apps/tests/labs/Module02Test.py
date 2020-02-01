import unittest
from labs.module02.TempSensorEmulatorTask import temperaturegen
from labs.module02.SmtpClientConnector import smtpconnect
import random
from labs.common.SensorData import SensorData
from sre_compile import isstring
import urllib.request


class Module02Test(unittest.TestCase):
	smtp_object = smtpconnect()  # Creating Instances of Classes Required
	data_object = SensorData()
	x = 0 
	
	def setUp(self):	
		self.x = temperaturegen.getSensorData(self)   
		self.data_object.addValue(self.x)  # Passing Generated Values Into SensorData Classs
	
	def testgeneratedtemperature(self):
		self.assertTrue(temperaturegen.getSensorData(self) >= 0.0 and temperaturegen.getSensorData(self) <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(temperaturegen.getSensorData(self), int), "Its not a Integer ")

												  # Checking Generated Temperature is float & within range
	def testPublishMessage(self):											  
		self.assertTrue(isinstance(self.smtp_object.getfromAddr(), str), "Its not a String ")  # Test Case to check valid mail
		self.assertTrue(isinstance(self.smtp_object.gettoAddr(), str), "Its not a String ")
		self.assertTrue(isinstance(self.smtp_object.getmsgBody(), str), "Its not a String ")
		self.assertTrue(self.connect("https://www.google.com"))

	def connect(self, host):  # Internet connectivity checker
	    try:
	        urllib.request.urlopen(host) 
	        return 1
	    except:
	        return 0
	

if __name__ == "__main__":
	unittest.main()  
