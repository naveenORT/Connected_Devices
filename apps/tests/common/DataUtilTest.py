import unittest
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module05.SensorDataManager import SensorDataManager
from labs.common.PersistenceUtil import util 
from labs.common.AData import AData
from labs.module05.TempSensorAdaptorTask import data_object
import redis
'''
* This class is for testing DataUtility tools which is used for converting from/to SensorData/ActuatorData to/from JSON string
'''


class DataUtilTest(unittest.TestCase):

	'''
	* Starting up essential class functions & threads for the purpose of testing 
	'''

	def setUp(self):
		self.msa = MultiSensorAdaptor()
		self.msa.start()
		self.sdm = SensorDataManager()
		self.sdm.start()
		self.redis_server = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
	
	'''
	* Function for testing whether sensordata is converted into JSON string 
	'''
		
	def testsensordatatojson(self):
		self.assertTrue(isinstance(util.sensordatatojson(data_object), str), "Not an actuator_data")

	'''
	* Function for testing whether json string is converted into actuatordata 
	'''

	def testjsontoactuatordata(self):
		self.assertTrue(isinstance(util.jsonToActuatorData(self.redis_server.get(str(1))), AData), "Not an actuator_data")

	
if __name__ == "__main__":
	unittest.main()
