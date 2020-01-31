import unittest
from labs.common.SensorData import SensorData
from labs.module02.TempSensorEmulatorTask import temperaturegen
class SensorDataTest(unittest.TestCase):
	
	sensor_object = SensorData()

	def setUp(self):
		self.sensor_object.addValue(temperaturegen.getSensorData(self))
	
	def tearDown(self):
		self.sensor_object = SensorData()
	
	def testcurvalue(self):
		self.assertTrue(isinstance(self.sensor_object.getcurvalue(), int), "Its not a integer ")
		
	def testavgvalue(self):
		self.assertTrue(isinstance(self.sensor_object.getavgvalue(), float), "Its not a float")	

	def testminvalue(self):	
		self.assertTrue(isinstance(self.sensor_object.getminvalue(), int), "Its not a Integer ")
	
	def testmaxvalue(self):	
		self.assertTrue(isinstance(self.sensor_object.getmaxvalue(), int), "Its not a Integer ")
		
	def testcountvalue(self):
		self.assertTrue(isinstance(self.sensor_object.gettotvalue(), int), "Its not a Integer ")	
	
	def testtotalvalue(self):
		self.assertTrue(isinstance(self.sensor_object.gettotvalue(), int), "Its not a Integer ")	
		

if __name__ == "__main__":
	unittest.main()