from _ast import If


class DeviceData():
    
    def setArduino1_status(self, input):
        self.arduino1_status = input
        
    def setArduino2_status(self, input):
        self.arduino2_status = input
        
    def setMem_Util(self, input):
        self.Mem_Util = input
        
    def setCpu_Util(self, input):
        self.Cpu_Util = input
        
    def getArduino1_status(self):
        if (self.arduino1_status == True):
            return 1
        if (self.arduino1_status == False):
            return 0
    def getArduino2_status(self):
        if (self.arduino2_status == True):
            return 1
        if (self.arduino2_status == False):
            return 0
    
    def getMem_Util(self):
        return self.Mem_Util
    
    def getCpu_Util(self):
        return self.Cpu_Util
    
