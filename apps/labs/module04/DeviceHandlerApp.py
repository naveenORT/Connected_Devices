'''
Created on Feb 14, 2020
@author: Naveen Rajendran
'''
from labs.module04.SensorDataManager import SensorDataManager
from labs.module04.MultiSensorAdaptor import MultiSensorAdaptor    


def main():

    msa = MultiSensorAdaptor()
    msa.start()

    manager_object = SensorDataManager()
    manager_object.start()

    
main()    
