import unittest
from labs.module07.CoAPClientConnector import CoAP_Server
from labs.module07.SensorDataManager import SensorDataManager
from labs.module07.MultiSensorAdaptor import MultiSensorAdaptor    
from labs.module07.TempSensorAdaptorTask import coap
import time

"""
Test class for all requisite Module07 functionality
"""


class Module07Test(unittest.TestCase):

	"""
	
	"""

	def setUp(self):
		'''
		* Thread for sensing values
		'''
		self.msa = MultiSensorAdaptor()  # Thread 1
		self.msa.start()  # Starting Thread
		'''
		* Thread for performing actuation based on values sensed
		'''
		self.manager_object = SensorDataManager()  # Thread 2
		self.manager_object.start()  # Starting Thread 

	"""
	
	"""

	def testPOST(self):
		time.sleep(5)
		self.assertTrue(coap.get_post_flag())
		
	def testPUT(self):
		time.sleep(5)
		self.assertTrue(coap.get_put_flag())

	def testGET(self):
		self.assertTrue(coap.get_del_flag() == False)
	
	def testDELETE(self):
		self.assertTrue(coap.get_del_flag() == False)

	
if __name__ == "__main__":
	unittest.main()
