'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
import threading
from labs.module02.SmtpClientConnector import smtpconnect
from labs.common.ConfigUtil import ConfigUtil
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.SensorData import SensorData
from labs.module04.HumiditySensorAdaptorTask import humidity_data_object
from labs.module04.TempSensorAdaptorTask import data_object
from labs.module04.HI2CSensorAdaptorTask import i2c_data_object
import time


class SensorDataManager(threading.Thread):    
    
    def __init__(self):
        threading.Thread.__init__(self)    
    
    def run(self):    
        time.sleep(4)
        while SensorDataManager.is_alive(self):
            time.sleep(3)
            self.trigger_actuation()            
            

    def trigger_actuation(self):
            haa = MultiActuatorAdaptor()        

    def handleActuatorData(self):   
        
        if(humidity_data_object.getActuationStae() is  True):
            return True

        if(i2c_data_object.getActuationStae() is  True):
            return True

        else:
            return False
        '''
        if(i2c_data_object.getActuationStae() is  True):
            return True
        '''
        
