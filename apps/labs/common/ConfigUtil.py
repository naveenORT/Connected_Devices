'''
Created on Jan 23, 2020
@author: Naveen Rajendran
''' 
from configparser import ConfigParser

class ConfigUtil:
       
    config = ConfigParser()
    
    def __init__(self,path):
        self.path = path
        self.loadConfig(path)
    
    def getValues(self,section,key):     
        return self.config.get(section,key)
   
    def hasSection(self,sec_name):
        if self.config.has_section(sec_name):
            return 1
    
    def loadConfig(self,path):   
        self.config.read(path)
    
    def getpath(self):
        return self.path
    
    
    def hasConfig(self):     
        try:
            f = open(self.path)
            return 1
        except IOError:
            print("File not accessible")
        finally:
            f.close()

