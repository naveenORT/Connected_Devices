import unittest
from labs.common.SensorData import SensorData
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
class SensorDataTest(unittest.TestCase):
	
	sensor_object = SensorData()  # Creating object of SensorData Class

	def setUp(self):
		self.x = TempSensorAdaptorTask(10)
		self.x.start()
		self.sensor_object.addValue(self.x.getSensorData())
	
	def tearDown(self):
		self.sensor_object = SensorData()
	
	def testcurvalue(self):
		self.assertTrue(self.sensor_object.getcurvalue() >= 0.0 and self.sensor_object.getcurvalue() <= 100.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getcurvalue(), float), "Its not a float ") # Checking Current Value is float
		
	def testavgvalue(self):
		self.assertTrue(self.sensor_object.getavgvalue() >= 0.0 and self.sensor_object.getavgvalue() <= 100.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getavgvalue(), float), "Its not a float")	# Checking average Value is float

	def testminvalue(self):	
		self.assertTrue(self.sensor_object.getminvalue() >= 0.0 and self.sensor_object.getminvalue() <= 100.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getminvalue(), float), "Its not a float ") # Checking min value is float
	
	def testmaxvalue(self):	
		self.assertTrue(self.sensor_object.getmaxvalue() >= 0.0 and self.sensor_object.getmaxvalue() <= 100.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.getmaxvalue(), float), "Its not a float ") # Checking max value is float
		
	def testcountvalue(self):
		self.assertTrue(self.sensor_object.getsamplecount() >= 0.0 and self.sensor_object.getsamplecount() <= 30.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.gettotvalue(), float), "Its not a float ")	# Checking count value is float
	
	def testtotalvalue(self):
		self.assertTrue(self.sensor_object.gettotvalue() >= 0.0 and self.sensor_object.gettotvalue() <= 1000.0  , "Not in RANGE")
		self.assertTrue(isinstance(self.sensor_object.gettotvalue(), float), "Its not a float ")	# Checking total value is float
		

if __name__ == "__main__":
	unittest.main()