import unittest
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module04.SensorDataManager import SensorDataManager
from labs.module04.HI2CSensorAdaptorTask import i2c_data_object
from labs.module04.HumiditySensorAdaptorTask import humidity_data_object
import time

class Module04Test(unittest.TestCase):

	def setUp(self):
		self.msa = MultiSensorAdaptor()
		self.msa.start()
		self.sdm = SensorDataManager()
		self.sdm.start()
		time.sleep(3)
	
	def test_I2Csensordata(self):
		self.assertTrue(isinstance(self.msa.geti2cobject().getSensorData(), float), "Not a float")

	def test_APIsensordata(self):	
		self.assertTrue(isinstance(self.msa.getAPIobject().getSensorData(), float), "Not a float")

	def test_sensor_data_handler(self):
		y = self.sdm.handle_sensordata(i2c_data_object)
		z = self.sdm.handle_sensordata(humidity_data_object)
		self.assertTrue(isinstance(y, bool), "Not a Boolean")
		self.assertTrue(isinstance(z, bool), "Not a Boolean")

	def test_update_actuator(self):
		time.sleep(10)
		x = self.sdm.get_maaadaptor()
		self.assertTrue(isinstance(x.update_Actuator(x.getapi_actobj()), bool), "Not Boolean")
		self.assertTrue(isinstance(x.update_Actuator(x.geti2c_actobj()), bool), "Not Boolean")


if __name__ == "__main__":
	unittest.main()
