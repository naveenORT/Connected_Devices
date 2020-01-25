import unittest
from labs.module01.SystemMemUtilTask import memutil
from labs.module01.SystemCpuUtilTask import cpuutil


class Module01Test(unittest.TestCase):

	def testMemUtilization(self):
		self.assertTrue(isinstance(memutil.getSensorData(self), float), "Its not a float ")  # checking the value is float
		self.assertTrue(memutil.getSensorData(self) >= 0.0 and memutil.getSensorData(self) <= 100.0  , "Not in RANGE")  # checking the value is range 
		pass

	def testCpuUtilization(self):
		self.assertTrue(isinstance(cpuutil.getSensorData(self), float), "Its not a float")  # checking the value is float
		self.assertTrue(cpuutil.getSensorData(self) >= 0.0 and cpuutil.getSensorData(self) <= 100.0  , "Not in RANGE")  # checking the value is range
		pass


if __name__ == "__main__":
	unittest.main()  # Calling unittest
