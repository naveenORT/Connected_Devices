'''
Created on Apr 8, 2020


@author: Naveen Rajendran
'''
from labs.module09.SensorHandlerApp import SensorHandlerApp
import logging

logging = logging()
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def main():
      
    x = SensorHandlerApp()
    x.start()
    
    
main()
