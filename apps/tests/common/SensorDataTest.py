import unittest
from labs.common.SensorData import SensorData
from labs.module02.TempSensorEmulatorTask import temperaturegen
class SensorDataTest(unittest.TestCase):
	
	sensor_object = SensorData()  # Creating object of SensorData Class

	def setUp(self):
		self.sensor_object.addValue(temperaturegen.getSensorData(self))
	
	def tearDown(self):
		self.sensor_object = SensorData()
	
	def testcurvalue(self):
		self.assertTrue(self.sensor_object.getcurvalue() >= 0.0 and self.sensor_object.getcurvalue() <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getcurvalue(), int), "Its not a float ") # Checking Current Value is float
		
	def testavgvalue(self):
		self.assertTrue(self.sensor_object.getavgvalue() >= 0.0 and self.sensor_object.getavgvalue() <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getavgvalue(), float), "Its not a float")	# Checking average Value is float

	def testminvalue(self):	
		self.assertTrue(self.sensor_object.getminvalue() >= 0.0 and self.sensor_object.getminvalue() <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getminvalue(), int), "Its not a float ") # Checking min value is float
	
	def testmaxvalue(self):	
		self.assertTrue(self.sensor_object.getmaxvalue() >= 0.0 and self.sensor_object.getmaxvalue() <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getmaxvalue(), int), "Its not a float ") # Checking max value is float
		
	def testcountvalue(self):
		self.assertTrue(self.sensor_object.getsamplecount() >= 0.0 and self.sensor_object.getsamplecount() <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.gettotvalue(), int), "Its not a float ")	# Checking count value is float
	
	def testtotalvalue(self):
		self.assertTrue(self.sensor_object.gettotvalue() >= 0.0 and self.sensor_object.gettotvalue() <= 1000.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.gettotvalue(), int), "Its not a float ")	# Checking total value is float
		

if __name__ == "__main__":
	unittest.main()