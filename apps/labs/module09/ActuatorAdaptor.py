'''
Created on Apr 16, 2020

@author: Naveen Rajendran
'''
class ActuatorAdaptor():
    
    def __init__(self):
        self.relay_status = False
        
    def setRelay(self,input):
        self.relay_status = input
    
    def getRelay(self):
        return self.relay_status