import unittest
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module05.SensorDataManager import SensorDataManager
from labs.common.PersistenceUtil import util 
from labs.common.AData import AData
from labs.module05.TempSensorAdaptorTask import data_object
class DataUtilTest(unittest.TestCase):

	def setUp(self):
		self.msa = MultiSensorAdaptor()
		self.msa.start()
		self.sdm = SensorDataManager()
		self.sdm.start()
	
	def testjsontoactuatordata(self):
		self.assertTrue(isinstance(util.jsonToActuatorData(self.sdm.get_alo().get_x_jsonactdata()), AData),"Not an actuator_data")
		
	def testsensordatatojson(self):
		self.assertTrue(isinstance(util.sensordatatojson(data_object), str),"Not an actuator_data")

if __name__ == "__main__":
	unittest.main()
