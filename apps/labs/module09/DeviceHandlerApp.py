'''
Created on Apr 8, 2020


@author: Naveen Rajendran
'''
from labs.module09.SensorHandlerApp import SensorHandlerApp
import logging

def main():
    
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")

    x = SensorHandlerApp()
    x.start()
    
    
main()
