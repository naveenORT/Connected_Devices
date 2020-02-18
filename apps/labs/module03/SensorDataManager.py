'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''

import threading
import time 
import logging
from labs.module02.SmtpClientConnector import smtpconnect
from labs.module03.TempSensorAdaptorTask import data_object
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.common.ConfigUtil import ConfigUtil


class SensorDataManager(threading.Thread):

    '''
    * Class constructor which instantiates instances from SmtpClientConnector & ConfigUtil class   
    '''

    def __init__(self):  # Constructor
        threading.Thread.__init__(self)
        SensorDataManager.setDaemon(self, True)
        self.nominal_temp = ConfigUtil(r"/home/pi/workspace/iot-device/apps/labs/common/ConnectedDevicesConfig.props")
        self.temp_set_point = self.nominal_temp.getValues("device", "nominalTemp")  # loading nominal temperature value from config file9
        self.message = ''        

    '''
    * This function obtains temperature values recorded in SensorData class & compares current temperature value with nominal temp
      value loaded from config file stored in hard-disk. If temperature higher than nominal is recorded it calls send notification
      function 
    '''

    def trigger_notification(self):
        if (data_object.getcurvalue() >= float(self.temp_set_point)):  # comparing current value with nominal value       
            self.sendNotification() 
        else: 
            return 

    '''   
    * This module facilitates in establishing smtp server by invoking smtpclientconnector function. It uses publishMessage function
      to send message body to respective client 
    '''

    def sendNotification(self):  # Function to Publish Alerts As Mail
        smtp_object = smtpconnect()    
        self.message = "\n Time Recorded : " + (str)((data_object.gettimestamp())) + "\n Current : " + (str)(data_object.getcurvalue()) + "\n Average : " + (str)(data_object.getavgvalue()) + "\n Samples : " + (str)(data_object.getsamplecount()) + "\n Minimum : " + (str)(data_object.getminvalue()) + "\n Maximum : " + (str)(data_object.getcurvalue())
        if(data_object.getcurvalue() < float(self.temp_set_point)):
            logging.info("Current temperature is " + str(float(self.temp_set_point) - data_object.getcurvalue()) + "C lesser than nomainal temp ")
        if(data_object.getcurvalue() > float(self.temp_set_point)):
            logging.info("Current temperature is " + str(data_object.getcurvalue() - float(self.temp_set_point)) + "C greater than nomainal temp ")
        
        smtp_object.publishMessage("Temperature Alert", self.message)

    '''
    * Runnable function, responsible for instantiation of actuator & notifier function
    '''

    def run(self):
        while SensorDataManager.is_alive(self):
            self.trigger_notification()
            x = TempActuatorAdaptor()
            time.sleep(3)
    
