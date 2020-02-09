'''
Created on Feb 6, 2020
@author: Naveen Rajendra
'''
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
   

def main():    

    temp_sensor_object = TempSensorAdaptor()    
    alarm_trigger = SensorDataManager()  
    alarm_trigger.start()  
    
    while True:
        pass
main()        
