import unittest
from labs.module09.GatewayHandlerApp import GatewayHandlerApp
import time

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = GatewayHandlerApp()
		self.x.start()
	
	def testSensorData(self):
		
		pass








if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()