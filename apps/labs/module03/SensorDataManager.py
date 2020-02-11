'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
import threading
import time 
from labs.module02.SmtpClientConnector import smtpconnect
from labs.module03.TempSensorAdaptorTask import data_object
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
from labs.common.ConfigUtil import ConfigUtil

"""
**************************************************Module Description ***********************************************************
* This module handles a thread that executes mail alert triggering and actuation of LED’s on sense hat. SensorDataManager module 
  retrieves temperature data from SensorData module by instantiating its object used by TempSensorAdaptorTask class
* Also it reads nominal temp value stored in ConnectedDevicesConfig.props file using ConfigUtil class. 
* After fetching nominal temperature value  it compares current value sensed using getCurvalue () in send notification function
* Once the sensed temperature is recorded above nominal temperature, e-mail alert is sent with help of SmtpClientConnector 
* While performing alarm triggering functions, it also invokes TempActuatorAdaptor class 
*********************************************************************************************************************************
"""


class SensorDataManager(threading.Thread):

    """
    * Class constructor which instantiates instances from SmtpClientConnector & ConfigUtil class   
    """

    def __init__(self):  # Constructor
        threading.Thread.__init__(self)
        SensorDataManager.setDaemon(self, True)
        self.nominal_temp = ConfigUtil(r"C:\Users\Naveen Rajendran\Desktop\MS COURSE\CSYE-6530 CONNECTED DEVICES WORKSPACE\iot-device\apps\labs\common\ConnectedDevicesConfig.props")
        self.temp_set_point = self.nominal_temp.getValues("device", "nominalTemp")  # loading nominal temperature value from config file
        self.message = ''        

    """
    * This function obtains temperature values recorded in SensorData class & compares current temperature value with nominal temp
      value loaded from config file stored in hard-disk. If temperature higher than nominal is recorded it calls send notification
      function 
    """

    def trigger_notification(self):
        if (data_object.getcurvalue() >= float(self.temp_set_point)):  # comparing current value with nominal value       
            self.sendNotification() 
        else: 
            return 

    """   
    * This module facilitates in establishing smtp server by invoking smtpclientconnector function. It uses publishMessage function
      to send message body to respective client 
    """

    def sendNotification(self):  # Function to Publish Alerts As Mail
        smtp_object = smtpconnect()    
        self.message = "\n Time Recorded : " + (str)((data_object.gettimestamp())) + "\n Current : " + (str)(data_object.getcurvalue()) + "\n Average : " + (str)(data_object.getavgvalue()) + "\n Samples : " + (str)(data_object.getsamplecount()) + "\n Minimum : " + (str)(data_object.getminvalue()) + "\n Maximum : " + (str)(data_object.getcurvalue())
        smtp_object.publishMessage("Temperature Alert", self.x)

    """
    * Runnable function, responsible for instantiation of actuator & notifier function
    """

    def run(self):
        while SensorDataManager.is_alive(self):
            self.trigger_notification()
            x = TempActuatorAdaptor()
            time.sleep(3)
    
