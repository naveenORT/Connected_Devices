import unittest
from labs.common.ActuatorData import ActuatorData
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
   
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
"""
*******************Module Description***************************************************************************
This class checks for any errors in value processed or logged by ActuatorData class, which logs the actuator data.
Inputs checked here includes command, sensor_name & actuator_status
****************************************************************************************************************
"""
class ActuatorDataTest(unittest.TestCase):

	'''
	* Setting up the required classes for test, 
	1.)TempSensorAdaptor - Senses the temperature value from environment
	2.)SensorDataManager - Triggers mail_notification & Triggers Actuation
	3.)TempActuatorAdaptor - Creates instance of ActuatorData class used to log actuator status 
	'''
	
	def setUp(self):
		self.temp_sensor_object = TempSensorAdaptor()
		self.alarm_trigger = SensorDataManager() 
		self.x = TempActuatorAdaptor()
		self.y = self.x.getActuator_obj()
	
	'''
	Gets the input of sensor name given by user & checks whether its string or not 
	'''
	def testSensorName(self):
		self.assertTrue(isinstance(self.y.getName(), str), "Not a String") # Function to check sensor name is string or not
	
	'''
	Gets the status_of_actuator from ActuatorData class & checks whether its string or not 
	'''
	def testActuatorStatus(self):
		self.assertTrue(isinstance(self.y.get_current_actuator_status(), str), "Not a String") # Function to check actuator_status is string or not
	
	'''
	Gets input command  from ActuatorData class & checks whether its string or not 
	'''
	def testCommand(self):	
		self.assertTrue(isinstance(self.y.get_command(), str), "Not a String") # Function to check command is string or not


if __name__ == "__main__":
	unittest.main()