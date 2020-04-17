
class DeviceData():
    
    def setArduino1_status(self, input):
        if (input == True):
            self.arduino1_status = 1
        else:
            self.arduino1_status = 0
    
    def setArduino2_status(self, input):
        if (input == True):
            self.arduino2_status = 1
        else:
            self.arduino2_status = 0
        
    def setMem_Util(self, input):
        self.ram = input
        
    def setCpu_Util(self, input):
        self.cpu = input
        
    def getArduino1_status(self):
        return self.arduino1_status
    
    def getArduino2_status(self):
        return self.arduino2_status
    
    def getMem_Util(self):
        return self.ram
    
    def getCpu_Util(self):
        return self.cpu
    
