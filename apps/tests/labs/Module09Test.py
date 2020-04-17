import unittest
from labs.module09.GatewayHandlerApp import GatewayHandlerApp
import time

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = GatewayHandlerApp()
	
	
	def testSensorData(self):
		exp1 = self.x.getArduino_Receiver_Obj().getSensorData_object()
		self.assertTrue(isinstance(exp1.getCorona(),float))
		pass








if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()