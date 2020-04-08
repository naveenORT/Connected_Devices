'''
Created on Apr 8, 2020


@author: Naveen Rajendran
'''
from labs.module09.SensorHandlerApp import SensorHandlerApp
import logging

def main():
    
    logging.info("Sensor_Logging_Started!!!")
    x = SensorHandlerApp()
    x.start()
    
    
main()
