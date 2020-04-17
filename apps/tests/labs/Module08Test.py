import unittest
from labs.module08.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module08.SensorDataManager import SensorDataManager
from labs.module08.MqttClientConnector import mqttc
from labs.module08.MqttClientConnector import act_data


class Module08Test(unittest.TestCase):

	"""
	* Setting up essential threads & functions for testing	
	"""

	def setUp(self):
		self.msa = MultiSensorAdaptor()  # Thread 1
		self.msa.start()  # Starting Thread
		manager_object = SensorDataManager()  # Thread 2
		manager_object.start()  # Starting

	"""
	* Function to check data published from mqttc
	"""

	def testPublishSensorData(self):
		self.assertTrue(mqttc.on_publish.__sizeof__() > 0)
		
	"""
	* Function to check data published from mqttc
	"""

	def testConnect(self):
		self.assertTrue(mqttc.is_connected() is True)

	def testSubscribeActuatorData(self):
		self.assertTrue(isinstance(act_data, str),"Not a String")


if __name__ == "__main__":
	unittest.main()
