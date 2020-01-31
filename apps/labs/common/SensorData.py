'''
Created on Jan 23, 2020
@author: Naveen Rajendran
'''
from datetime import datetime 
import logging
  
class SensorData():
    
    timeStamp = None
    name = 'Not set'
    curValue = 0
    avgValue = 0
    minValue = 0
    maxValue = 0
    totValue = 0
    sampleCount = 0
     
    def __init__(self):
        self.timeStamp = str(datetime.now())
    
    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = newVal
        self.totValue += newVal
    
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
        
        if (self.totValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount

        curValue = "curValue = " + str(self.curValue) 
        avgValue = "avgValue = " + str(self.avgValue)
        minValue = "minValue =" + str(self.minValue)
        maxValue = "maxValue =" + str(self.maxValue)
        totValue = "totValue =" + str(self.totValue)
        sampleCount = "sample count =" + str(self.sampleCount)
        
        logging.info('\n')
        logging.info(curValue)        
        logging.info(avgValue)
        logging.info(minValue)
        logging.info(maxValue)
        logging.info(totValue)
        logging.info(sampleCount)
    
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