import unittest
from labs.common.ActuatorData import ActuatorData
from labs.module04.SensorDataManager import SensorDataManager
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor  
import time
'''
******************************************Module Description****************************************************
This class checks for any errors in value processed or logged by ActuatorData class, which logs the actuator data.
Inputs checked here includes command, sensor_name & actuator_status
****************************************************************************************************************
'''


class ActuatorDataTest(unittest.TestCase):

	'''
	* Setting up the required classes for test, 
	1.)MutiSensorSensorAdaptor - Senses relative humidity value from environment via two different threads
	2.)SensorDataManager - Triggers actuation based on values from MultiSensorAdaptorTest 
	'''
	
	def setUp(self):
		self.msa = MultiSensorAdaptor()
		self.msa.start()
		time.sleep(1)
		self.manager_object = SensorDataManager()
		self.manager_object.start()
		time.sleep(10)
		self.x = self.manager_object.get_maaadaptor().getapi_actobj()
		self.y = self.manager_object.get_maaadaptor().getapi_actobj()

	'''
	Gets the input of sensor name given by user & checks whether its string or not 
	'''

	def testSensorName(self):
		time.sleep(2)
		self.assertTrue(isinstance(self.x.getName(), str), "Not a String")  # Function to check sensor name is string or not
		self.assertTrue(isinstance(self.y.getName(), str), "Not a String")  # Function to check sensor name is string or not

	'''
	Gets the status_of_actuator from ActuatorData class & checks whether its string or not 
	'''

	def testActuatorStatus(self):
		time.sleep(2)
		self.assertTrue(isinstance(self.x.get_current_actuator_status(), str), "Not a String")  # Function to check actuator_status is string or not
		self.assertTrue(isinstance(self.y.get_current_actuator_status(), str), "Not a String")

	'''
	Gets input command  from ActuatorData class & checks whether its string or not 
	'''

	def testCommand(self):	
		time.sleep(2)
		self.assertTrue(isinstance(self.x.get_command(), str), "Not a String")  # Function to check command is string or not
		self.assertTrue(isinstance(self.y.get_command(), str), "Not a String")


if __name__ == "__main__":
	unittest.main()
