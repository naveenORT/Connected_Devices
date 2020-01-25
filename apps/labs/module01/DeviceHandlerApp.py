'''
Created on Jan 14, 2020
@author: Naveen Rajendran
'''
from labs.module01 import SystemPerformanceAdaptor 
import logging

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    obj = SystemPerformanceAdaptor.SystemPerformanceAdaptor(10)        #Calling SystemPerformanceAdaptor Class Instance 
    obj.start()                                                        #Starting Thread               
    
main()