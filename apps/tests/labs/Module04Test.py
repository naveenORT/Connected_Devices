import unittest
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module04.SensorDataManager import SensorDataManager
from labs.module04.HI2CSensorAdaptorTask import i2c_data_object
from labs.module04.HumiditySensorAdaptorTask import humidity_data_object
import time
'''
* This class performs tests public functions or methods associated within moudle04 lab work
'''


class Module04Test(unittest.TestCase):
	
	'''
	* Setting up threads required for testing
	'''

	def setUp(self):
		self.msa = MultiSensorAdaptor()  # Sensor Thread
		self.msa.start()
		self.sdm = SensorDataManager()  # Actuator Thread
		self.sdm.start()
		time.sleep(3)
	
	'''
	* testing sensordata object for type & value range
	'''

	def test_I2Csensordata(self):
		self.assertTrue(isinstance(self.msa.geti2cobject().getSensorData(), float), "Not a float")
		self.assertTrue(self.msa.geti2cobject().getSensorData() >= 0 and self.msa.geti2cobject().getSensorData() <= 100, "Not a float")
	
	'''
	* testing sensordata object for type & value range
	'''

	def test_APIsensordata(self):	
		self.assertTrue(isinstance(self.msa.getAPIobject().getSensorData(), float), "Not a float")
		self.assertTrue(self.msa.getAPIobject().getSensorData() >= 0 and self.msa.getAPIobject().getSensorData() <= 100, "Not a float")
	
	'''
	* comparing api sensor value & i2c sensor value, for checkings computed difference is within range
	'''

	def test_compare_data(self):	
		self.assertTrue(abs(self.msa.geti2cobject().getSensorData() - self.msa.getAPIobject().getSensorData()) <= 1, "Not Matching")

	'''
	* testing whether sensordata is handled properly for actuation
	'''

	def test_sensor_data_handler(self):
		y = self.sdm.handle_sensordata(i2c_data_object)
		z = self.sdm.handle_sensordata(humidity_data_object)
		self.assertTrue(isinstance(y, bool), "Not a Boolean")
		self.assertTrue(isinstance(z, bool), "Not a Boolean")

	'''
	* testing whether actuator data is updating status of actuator  
	'''

	def test_update_actuator(self):
		time.sleep(10)
		x = self.sdm.get_maaadaptor()
		self.assertTrue(isinstance(x.update_Actuator(x.getapi_actobj()), bool), "Not Boolean")
		self.assertTrue(isinstance(x.update_Actuator(x.geti2c_actobj()), bool), "Not Boolean")


if __name__ == "__main__":
	unittest.main()
