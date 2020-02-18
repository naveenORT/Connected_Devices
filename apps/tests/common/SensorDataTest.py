import unittest
from labs.module04.SensorDataManager import SensorDataManager
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor  
import time
'''
******************************************************Module Description************************************************************
-> This test module checks parameters & public functions associated with SensorData class, which helps in recording Humidity sensor 
   values generated by sensor coupled with iot-device 
************************************************************************************************************************************
'''


class SensorDataTest(unittest.TestCase):
	'''
	* Setting up the required classes for test, 
    1.)MutiSensorSensorAdaptor - Senses relative humidity value from environment via two different threads
    2.)SensorDataManager - Triggers actuation based on values from MultiSensorAdaptorTest 
    
	''' 

	def setUp(self):
            msa = MultiSensorAdaptor()
            msa.start()
            manager_object = SensorDataManager()
            manager_object.start()
            time.sleep(10)
            self.api_sensor_object = msa.getAPIobject().getApiSensorDataObject()   
            self.i2c_sensor_object = msa.geti2cobject().getI2Csensordataobject()

	''' 
	* This function gets current Humidity value recorded by Sensordata class and checks for its type associated & range 
	''' 
	
	def testcurvalue(self):
            self.assertTrue(self.api_sensor_object.getcurvalue() >= 0.0 and self.api_sensor_object.getcurvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.api_sensor_object.getcurvalue(), float), "Its not a float ")  # Checking Current Value is float
            self.assertTrue(self.i2c_sensor_object.getcurvalue() >= 0.0 and self.i2c_sensor_object.getcurvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.i2c_sensor_object.getcurvalue(), float), "Its not a float ")  # Checking Current Value is float

	''' 
	* This function gets average Humidity value recorded by Sensordata class and checks for its type associated & range 
	''' 	

	def testavgvalue(self):
            self.assertTrue(self.api_sensor_object.getavgvalue() >= 0.0 and self.api_sensor_object.getavgvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.api_sensor_object.getavgvalue(), float), "Its not a float")  # Checking average Value is float
            self.assertTrue(self.i2c_sensor_object.getavgvalue() >= 0.0 and self.i2c_sensor_object.getavgvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.i2c_sensor_object.getavgvalue(), float), "Its not a float")  # Checking average Value is float

	''' 
	* This function gets minimum Humidity value recorded by Sensordata class and checks for its type associated & range 
	''' 

	def testminvalue(self):	
            self.assertTrue(self.api_sensor_object.getminvalue() >= 0.0 and self.api_sensor_object.getminvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.api_sensor_object.getminvalue(), float), "Its not a float ")  # Checking min value is float
            self.assertTrue(self.i2c_sensor_object.getminvalue() >= 0.0 and self.i2c_sensor_object.getminvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.i2c_sensor_object.getminvalue(), float), "Its not a float ")  # Checking min value is float

	''' 
	* This function gets maximum Humidity value recorded by Sensordata class and checks for its type associated & range 
	''' 

	def testmaxvalue(self):	
            self.assertTrue(self.api_sensor_object.getmaxvalue() >= 0.0 and self.api_sensor_object.getmaxvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.api_sensor_object.getmaxvalue(), float), "Its not a float ")  # Checking max value is float
            self.assertTrue(self.i2c_sensor_object.getmaxvalue() >= 0.0 and self.i2c_sensor_object.getmaxvalue() <= 100.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.i2c_sensor_object.getmaxvalue(), float), "Its not a float ")

	''' 
	* This function gets count value recorded by Sensordata class and checks for its type associated & range 
	''' 

	def testcountvalue(self):
            self.assertTrue(self.api_sensor_object.getsamplecount() >= 0.0 and self.api_sensor_object.getsamplecount() <= 30.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.api_sensor_object.gettotvalue(), float), "Its not a float ")  # Checking count value is float
            self.assertTrue(self.i2c_sensor_object.getsamplecount() >= 0.0 and self.i2c_sensor_object.getsamplecount() <= 30.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.i2c_sensor_object.gettotvalue(), float), "Its not a float ")  # Checking count value is float

	''' 
	* This function gets total Humidity value recorded by Sensordata class and checks for its type associated & range 
	''' 

	def testtotalvalue(self):
            self.assertTrue(self.api_sensor_object.gettotvalue() >= 0.0 and self.api_sensor_object.gettotvalue() <= 1000.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.api_sensor_object.gettotvalue(), float), "Its not a float ")  # Checking total value is float
            self.assertTrue(self.i2c_sensor_object.gettotvalue() >= 0.0 and self.i2c_sensor_object.gettotvalue() <= 1000.0  , "Not in RANGE")
            self.assertTrue(isinstance(self.i2c_sensor_object.gettotvalue(), float), "Its not a float ")  # Checking total value is float


if __name__ == "__main__":
	unittest.main()  # Main Function
