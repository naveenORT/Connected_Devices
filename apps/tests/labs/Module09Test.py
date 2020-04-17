import unittest
from labs.module09.GatewayHandlerApp import GatewayHandlerApp
import time

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = GatewayHandlerApp()
	
	
	def testSensorData(self):
		exp1 = self.x.getArduino_Receiver_Obj().getSensorData_object()
		self.assertTrue(isinstance(exp1.getCorona(),int) and 0 < exp1.getCorona() < 100)
		self.assertTrue(isinstance(exp1.getResistence(),int) and 0 < exp1.getResistence() < 100)
		self.assertTrue(isinstance(exp1.getHumidity(),float) and 0 < exp1.getHumidity() < 100)
		self.assertTrue(isinstance(exp1.getMagFlux()),float  and 0 < exp1.getMagFlux() < 100)
		self.assertTrue(isinstance(exp1.getTemperature(),float) and 0 < exp1.getCorona() < 100)
		








if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()