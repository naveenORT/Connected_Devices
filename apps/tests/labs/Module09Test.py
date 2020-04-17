import unittest
from labs.module09.ArduinoDataReceiver import ArduinoDataReceiver
import time

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = ArduinoDataReceiver()
		time.sleep(5)
		self.x.start()
	
	def testSensorData(self):
		time.sleep(5)
		exp1= self.x.getSensorData_object()
		self.assertTrue(isinstance(exp1.getCorona(),float))
	








if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()