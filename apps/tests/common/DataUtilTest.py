import unittest
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module05.SensorDataManager import SensorDataManager
from labs.common.PersistenceUtil import util 
from labs.common.AData import AData
from labs.module05.TempSensorAdaptorTask import data_object
import redis
class DataUtilTest(unittest.TestCase):
	redis_Server = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
	
	def setUp(self):
		self.msa = MultiSensorAdaptor()
		self.msa.start()
		self.sdm = SensorDataManager()
		self.sdm.start()
	
		
	def testsensordatatojson(self):
		self.assertTrue(isinstance(util.sensordatatojson(data_object), str),"Not an actuator_data")
	def testjsontoactuatordata(self):
		self.assertTrue(isinstance(util.jsonToActuatorData(self.redis_server.get(str(1))), AData),"Not an actuator_data")
	
if __name__ == "__main__":
	unittest.main()
