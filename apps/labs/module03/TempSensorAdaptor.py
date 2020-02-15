'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module03.TempSensorAdaptorTask import data_object  
import logging
import threading
'''
****************************************************Module Description**************************************************************
* This module helps to start the thread of TempSensorAdaptorTask () class. Once TempSensorAdaptor object is created, a thread is 
   executed which helps in sensing environment temperature
************************************************************************************************************************************
'''


class TempSensorAdaptor(threading.Thread):
   
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("started logging")
        threading.Thread.__init__(self)
        self.sensor_object = TempSensorAdaptorTask(20)
        self.sensor_object.start()  # Starting Threaded Class Object

    '''    
    Standard getter function to return the instance of TempSensorAdaptor
    '''

    def getSensorobj(self):
        return self.sensor_object
