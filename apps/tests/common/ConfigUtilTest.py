import unittest
from labs.common.ConfigUtil import ConfigUtil
import os.path

"""
**************************************************Module Description*************************************************************
-> This test module performs tests public functions & parameters associated with ConfigUtil class
*********************************************************************************************************************************
"""


class ConfigUtilTest(unittest.TestCase):

	configobj = ''
	
	"""
	* Loading ConfigUtil class which takes directory of file ConnectedDevice.props as input
	"""  

	def setUp(self):
		self.configobj = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props")

	"""
	* Test function to check whether .props file is loaded with values required for operation
	"""  

	def testIsConfigDataLoaded(self):  # Test function to check file exists or not
		self.assertTrue(os.path.isfile(self.configobj.getpath()))

	"""
	* Test function to check whether .props file is loaded with section required for operation
	"""  

	def testHasSection(self):  # Test Function to check whether it has section
		self.assertTrue(self.configobj.hasSection("smtp.cloud"))

	"""
	* Test function to check whether .props file is having boolean properties required for operation
	"""  

	def testGetBooleanProperty(self):  # Test Function to check boolean property
		self.assertTrue(isinstance((bool)(self.configobj.getValues("smtp.cloud", "enableAuth")), bool), "Its not a bool ")
		self.assertTrue(isinstance((bool)(self.configobj.getValues("smtp.cloud", "enableCrypt")), bool), "Its not a bool ")

	"""
	* Test function to check whether .props file is loaded with integer properties required for operation
	"""  

	def testGetIntegerProperty(self):  # Test Function to check integer property
		self.assertTrue(isinstance((int)(self.configobj.getValues("smtp.cloud", "port")), int), "Its not a float ")
		self.assertTrue(isinstance((int)(self.configobj.getValues("device", "nominalTemp")), int), "Its not a float ")

	"""
	* Test function to check whether .props file is loaded with properties required for operation
	"""  

	def testgetProperty(self):
		self.assertTrue(self.configobj.getValues("smtp.cloud", "host"), "value does not exist")  # Test Function to Get Property
		self.assertTrue(self.configobj.getValues("smtp.cloud", "port"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "fromAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "toAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "toMediaAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "toTxtAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "AuthToken"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "enableAuth"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "enableCrypt"), "value does not exist")
		self.assertTrue(self.configobj.getValues("device", "nominalTemp"), "value does not exist")

	"""
	* Test function to check whether .props file is having values required for operation
	"""  

	def testhasProperty(self):
		self.assertTrue(self.hasproperty("port"), "property does not exist")  # Test function to check file has properties/not           
		self.assertTrue(self.hasproperty("host"), "property does not exist")
		self.assertTrue(self.hasproperty("fromAddr"), "property does not exist")
		self.assertTrue(self.hasproperty("toAddr"), "property does not exist")
		self.assertTrue(self.hasproperty("toMediaAddr"), "property does not exist")
		self.assertTrue(self.hasproperty("toTxtAddr"), "property does not exist")
		self.assertTrue(self.hasproperty("AuthToken"), "property does not exist")	
		self.assertTrue(self.hasproperty("enableAuth"), "property does not exist")
		self.assertTrue(self.hasproperty("enableCrypt"), "property does not exist")

	"""
	* public function to check whether .props file is loaded with properties required for functioning
	"""  

	def hasproperty(self, property_name):                                  
		if self.configobj.getValues("smtp.cloud", property_name):
			return True
		else:
			return False

	
if __name__ == "__main__":
	unittest.main()  # Main Function
