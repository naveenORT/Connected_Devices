'''
Created on Apr 8, 2020

@author: Naveen Rajendran
'''
from labs.project.SensorHandlerApp import SensorHandlerApp


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    opc_obj = OPC_Client()
    opc_obj.start()
    
