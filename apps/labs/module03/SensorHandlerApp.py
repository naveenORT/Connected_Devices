'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
   
'''
******************************************* Module Description *********************************************************
This module forms the main node of this application. It invokes two threads, one for sensing temperature from environment TempSensorAdaptor 
& another thread (SensorDataManager) for triggering e-mail alerts and actuation of LED on sense hat
These threads will be ran at specific intervals so that there can be a productive exchange of information from sensor thread
*************************************************************************************************************************
'''


def main():   

    temp_sensor_object = TempSensorAdaptor()  # Thread 1 - Temperature Sensing
    alarm_trigger = SensorDataManager()  # Thread 2 - Notification generator & actuation function class
    alarm_trigger.start()  
    
    while True:
        pass


main()        
