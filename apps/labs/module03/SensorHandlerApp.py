'''
Created on Feb 6, 2020
@author: Naveen Rajendran
'''
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
   

def main():    
    
    
    alarm_trigger = SensorDataManager()  
    alarm_trigger.start()
    
    temp_sensor_object = TempSensorAdaptor()    
    temp_sensor_object.start()
    
    
    while True:
        pass
main()        
