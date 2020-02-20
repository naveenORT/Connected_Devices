'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
from labs.module05.SensorDataManager import SensorDataManager
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor    
'''
* This module forms the main node of this application. It invokes two threads, one for polling humidity values from sensor & another 
thread for actuating led's based on sensor thread values. 
* These threads will be ran at specific intervals so that there can be a productive exchange of information
'''


def main():
    '''
    * Thread for sensing values
    '''
    msa = MultiSensorAdaptor()  # Thread 1
    msa.start()  # Starting Thread
    '''
    * Thread for performing actuation based on values sensed
    '''
    manager_object = SensorDataManager()  # Thread 2
    manager_object.start()  # Starting Thread 
    
    
main()    
