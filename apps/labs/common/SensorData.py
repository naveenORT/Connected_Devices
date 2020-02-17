'''
Created on Jan 23, 2020
@author: Naveen Rajendran
'''
from datetime import datetime 
from labs.common.ActuatorData import ActuatorData
import logging

  
class SensorData():
    
    timeStamp = None  # Initializing the parameters
    name = 'Not set'
    curValue = 0.0
    avgValue = 0.0
    minValue = 0.0 
    maxValue = 0.0
    totValue = 0.0
    sampleCount = 0
    Actuation_State = False
    
    def __init__(self):
        self.timeStamp = str(datetime.now())  # Constructor
    
    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = newVal
        self.totValue += newVal
        self.setAcutationState(True)
        
        if(self.sampleCount == 1):
            self.minValue = self.curValue
        
        elif (self.curValue < self.minValue):  # Assign Minimum Temperature Value
            self.minValue = self.curValue
        
        if (self.curValue > self.maxValue):  # Assign Maximum Temperature Value
            self.maxValue = self.curValue
        
        if (self.totValue != 0 and self.sampleCount > 0):  # Computing Average Value
            self.avgValue = self.totValue / self.sampleCount

        curValue = "curValue = " + str(round(self.curValue,2))  # converting all parameters to string type 
        avgValue = "avgValue = " + str(round(self.avgValue,2))
        minValue = "minValue =" + str(round(self.minValue,2))
        maxValue = "maxValue =" + str(round(self.maxValue,2))
        totValue = "totValue =" + str(round(self.totValue,2))
        sampleCount = "sample count =" + str(self.sampleCount)
        
        logging.info('\n')
        logging.info("-----------------------------------Values From =" + self.get_sensor_name()+ "---------------------------")
        logging.info(curValue)        
        logging.info(avgValue)
        logging.info(minValue)
        logging.info(maxValue)
        logging.info(totValue)
        logging.info(sampleCount)
        logging.info("_____________________________________________________________________________________________")
    
        
   
    def getcurvalue(self):
        return self.curValue
    
    def getavgvalue(self):
        return self.avgValue
    
    def getminvalue(self):
        return self.minValue
    
    def getmaxvalue(self):
        return self.maxValue
    
    def gettotvalue(self):
        return self.totValue
    
    def getsamplecount(self):
        return self.sampleCount
    
    def gettimestamp(self):
        return self.timeStamp
    
    def set_sensor_name(self, sensor_name):
        self.name = sensor_name
    
    def get_sensor_name(self):    
        return self.name
    
    def setAcutationState(self, in_value):    
        self.Actuation_State = in_value
        
    def getActuationStae(self):    
        return self.Actuation_State