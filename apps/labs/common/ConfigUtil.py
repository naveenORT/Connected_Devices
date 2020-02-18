'''
Created on Jan 23, 2020
@author: Naveen Rajendran
''' 
from configparser import ConfigParser
import logging


class ConfigUtil:
       
    config = ConfigParser()
    default_dir = r"home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props"

    def __init__(self, path):  # Constructor
        self.path = path
        self.loadConfig(path)
    
    def getValues(self, section, key):  # Function to extract values mapped along with keys    
        return self.config.get(section, key)
   
    def hasSection(self, sec_name):  # Function to check the existence of section
        if self.config.has_section(sec_name):
            return 1
        
    def loadConfig(self, path):  # Function to load config properties from the file
        try:
            if self.hasConfig():
                self.config.read(path, encoding=None)
            else:    
                self.config.read(self.default_dir)
        except:
            logging.info("File doesn't exist loading default")        
    
    def getpath(self):  # Function to get path name of config file
        return self.path
    
    def hasConfig(self):  # Checking the existence of config file in the harddisk     
        try:
            f = open(self.path)
            return 1
        except IOError:
            print("File not accessible")
        finally:
            f.close()

