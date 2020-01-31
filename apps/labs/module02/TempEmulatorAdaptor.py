'''
Created on Jan 23, 2020
@author: Naveen Rajendran
'''
import logging
import threading
from labs.module02.TempSensorEmulatorTask import temperaturegen

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("started logging")
    obj = temperaturegen(15,5)
    obj.start()
    while True:
        pass

main()