import unittest
from labs.module09.GatewayHandlerApp import GatewayHandlerApp

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = GatewayHandlerApp()


	def testSensorData(self):
		expression = self.x.getArduino_Receiver_Obj().getSensorData_object()
		self.assertTrue(isinstance(expression.getHumidity(),float))
		self.assertTrue(isinstance(expression.getCorona(),float))
		self.assertTrue(isinstance(expression.getCorona(),float))
		self.assertTrue(isinstance(expression.getCorona(), float))
		self.assertTrue(isinstance(expression.getCorona(), float))





















if __name__ == "__main__":
	unittest.main()
