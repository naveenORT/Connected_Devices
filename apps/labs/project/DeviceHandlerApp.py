'''
Created on Apr 2, 2020

@author: Naveen Rajendran
'''
import logging
from labs.project.OPC_Client import OPC_Client 

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(".started logging.")
    opc_obj = OPC_Client()
    opc_obj.start()
    
main()    
