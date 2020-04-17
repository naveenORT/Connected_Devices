import unittest
from labs.module09.GatewayHandlerApp import GatewayHandlerApp
import time

class Module09Test(unittest.TestCase):

	def setUp(self):
		self.x = GatewayHandlerApp()
	
	
	def testSensorData(self):
		exp1 = self.x.getArduino_Receiver_Obj().getSensorData_object()
		self.assertTrue(isinstance(exp1.getCorona(),int) and 0 < exp1.getCorona() < 100)
		self.assertTrue(isinstance(exp1.getResistence(),int) and 0 < exp1.getResistence() < 150)
		self.assertTrue(isinstance(exp1.getHumidity(),float) and 0 < exp1.getHumidity() < 100)
		self.assertTrue(isinstance(exp1.getMagFlux(),float)  and 0 < exp1.getMagFlux() < 100)
		self.assertTrue(isinstance(exp1.getTemperature(),float) and 0 < exp1.getCorona() < 160)
		
	def testDeviceData(self):
		exp2 = self.x.getArduino_Receiver_Obj().getDeviceData_object()
		self.assertTrue(isinstance(exp2.getCpu_Util(),float) and 0 < exp2.getCpu_Util() < 100)
		self.assertTrue(isinstance(exp2.getMem_Util(),float)  and 0 < exp2.getMem_Util() < 100)
		self.assertTrue(isinstance(exp2.getArduino1_status(),int) and 0 or 1)
		self.assertTrue(isinstance(exp2.getMem_Util(),int)  and 0 or 1)

	def testAlertData(self):
		exp3 = self.x.getSensorDataManager().getSMTP()
		self.assertTrue(isinstance(exp3.getmsgBody(),str))
	
	def ubidots_test(self):
		exp4 = self.x.getUbidotsCloudConnector()
		self.assertTrue(exp4.get_connected_flag() is True)
		self.assertTrue(exp4.get_publish_flag() is True)
		self.assertTrue(exp4.get_subscribe_flag() is True)
	
	def testactData(self):
		exp5 = self.x.getUbidotsCloudConnector().get_act_obj()
		self.assertTrue(exp5.getRelay() is True or False)


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()