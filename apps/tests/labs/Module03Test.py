import unittest
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
"""


"""


class Module03Test(unittest.TestCase):

	"""


	"""

	def setUp(self):
		self.temp_sensor_object = TempSensorAdaptorTask(10)    
	
	"""

	"""
	def testSensor_Temperature(self):
		self.assertTrue(0 < self.temp_sensor_object.getSensorData() < 100, "Not in Range")
		self.assertTrue(isinstance(self.temp_sensor_object.getSensorData(),float), "Not in Range")
		


if __name__ == "__main__":	
	unittest.main()
