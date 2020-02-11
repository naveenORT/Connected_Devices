import unittest
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
from labs.module02.SmtpClientConnector import smtpconnect

"""
************************************************Module Description***************************************************
* This test class tests the public function which helps to obtain temperature value from sensehat 
* It also performs tests on alert message sent from device to user's mail
*********************************************************************************************************************
"""


class Module03Test(unittest.TestCase):

	"""
	* Instantiating threads & objects required for testing this test module
	"""

	def setUp(self):
 		adaptor_object = TempSensorAdaptor()  # Thread object 1
 		self.temp_sensor_object = adaptor_object.getSensorobj()	
 		manager_object = SensorDataManager()  # Thread object 2
	 	manager_object.start()  # Starting thread
	 	self.message_object = smtpconnect()  # SMTP class object

	"""
	* This function tests temperature value received from sense hat's sensor by instantiating TempSensorAdaptor class
	"""

	def testSensor_Temperature(self):
		self.assertTrue(0 < self.temp_sensor_object.getSensorData() < 100, "Not in Range")          # Checking range
		self.assertTrue(isinstance(self.temp_sensor_object.getSensorData(), float), "Not in Range") # Checking type

	"""
	* This function tests message body which will be sent as mail by SensorDataManager class using SmtpClientConnector class, 
	  when temperature is recorded above nominal value loaded
	"""

	def testTriggerNotification(self):
		self.assertTrue(isinstance(self.message_object.getmsgBody(), str), "Not a string")          # Checking type


if __name__ == "__main__":	
	unittest.main()  # Main function 
