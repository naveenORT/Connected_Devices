import unittest
from labs.module06.SensorDataManager import SensorDataManager
from labs.module06.MultiSensorAdaptor import MultiSensorAdaptor    
from labs.module06.TempSensorAdaptorTask import mqttc 

"""
* This class is for the purpose of testing public functions associated with module06
"""


class Module06Test(unittest.TestCase):

	"""
	* Setting up essential threads & functions for testing	
	"""

	def setUp(self):
		msa = MultiSensorAdaptor()  # Thread 1
		msa.start()  # Starting Thread
		manager_object = SensorDataManager()  # Thread 2
		manager_object.start()  # Starting

	"""
	* Function to check data published from mqttc
	"""

	def testPublishSensorData(self):
		print(mqttc._on_publish.__sizeof__())
		self.assertTrue(mqttc._on_publish.__sizeof__() > 0)

	"""
	* Function to check data published from mqttc
	"""

	def testConnect(self):
		self.assertTrue(mqttc.is_connected() is True)


if __name__ == "__main__":
	unittest.main()
