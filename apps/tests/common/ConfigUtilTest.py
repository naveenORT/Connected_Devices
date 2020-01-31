import unittest
from labs.common.ConfigUtil import ConfigUtil
import os.path


class ConfigUtilTest(unittest.TestCase):

	configobj = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props")
	
	def testIsConfigDataLoaded(self):
		self.assertTrue(os.path.isfile(self.configobj.getpath()))

	def testHasSection(self):
		self.assertTrue(self.configobj.hasSection("smtp.cloud"))
	
	def testGetBooleanProperty(self):
		self.assertTrue(isinstance((bool)(self.configobj.getValues("smtp.cloud", "enableAuth")), bool), "Its not a bool ")
		self.assertTrue(isinstance((bool)(self.configobj.getValues("smtp.cloud", "enableCrypt")), bool), "Its not a bool ")
	
	def testGetIntegerProperty(self):
		self.assertTrue(isinstance((int)(self.configobj.getValues("smtp.cloud", "port")), int), "Its not a float ")
	
	def testgetProperty(self):
		self.assertTrue(self.configobj.getValues("smtp.cloud", "host"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "port"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "fromAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "toAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "toMediaAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "toTxtAddr"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "AuthToken"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "enableAuth"), "value does not exist")
		self.assertTrue(self.configobj.getValues("smtp.cloud", "enableCrypt"), "value does not exist")
	
	def testhasProperty(self):
		self.assertTrue(self.hasproperty("port"),"property does not exist")
		self.assertTrue(self.hasproperty("host"),"property does not exist")
		self.assertTrue(self.hasproperty("fromAddr"),"property does not exist")
		self.assertTrue(self.hasproperty("toAddr"),"property does not exist")
		self.assertTrue(self.hasproperty("toMediaAddr"),"property does not exist")
		self.assertTrue(self.hasproperty("toTxtAddr"),"property does not exist")
		self.assertTrue(self.hasproperty("AuthToken"),"property does not exist")	
		self.assertTrue(self.hasproperty("enableAuth"),"property does not exist")
		self.assertTrue(self.hasproperty("enableCrypt"),"property does not exist")
	
	
	def hasproperty(self, property_name):
		if self.configobj.getValues("smtp.cloud", property_name):
			return 1
		else:
			return 0
	
if __name__ == "__main__":
	unittest.main()
