'''
Created on Feb 14, 2020

@author: Naveen Rajendran
'''
import threading
from labs.module02.SmtpClientConnector import smtpconnect
from labs.common.ConfigUtil import ConfigUtil
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor

class SensorDataManager():
    
    def __init__(self):
        msa = MultiSensorAdaptor()
