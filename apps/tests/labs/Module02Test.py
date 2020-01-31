import unittest
from labs.module02.TempSensorEmulatorTask import temperaturegen
from labs.module02.SmtpClientConnector import smtpconnect
import random
from labs.common.SensorData import SensorData
from sre_compile import isstring

class Module02Test(unittest.TestCase):
	smtp_object = smtpconnect()    
	data_object = SensorData()
	
	def setUp(self):	
		x = temperaturegen.getSensorData(self)
		self.data_object.addValue(x)
	
	def testgeneratedtemperature(self):
		self.assertTrue(temperaturegen.getSensorData(self) >= 0.0 and temperaturegen.getSensorData(self) <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(temperaturegen.getSensorData(self), int), "Its not a Integer ")

	def testsendmail(self):
		message = ("Current Value:", self.data_object.getcurvalue(),
           			"Average Value:", self.data_object.getavgvalue() ,
             				"Samples:", self.data_object.getsamplecount() ,
           	   							"Min:", self.data_object.getminvalue() ,
           	      								"Max:", self.data_object.getcurvalue())
		y = str(message)
		self.assertTrue(isstring(y))

if __name__ == "__main__":
	unittest.main()  
