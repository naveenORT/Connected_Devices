'''
Created on Apr 9, 2020
@author: Naveen Rajendran
'''
from labs.module01.SystemMemUtilTask import memutil
from labs.module01.SystemCpuUtilTask import cpuutil
from labs.module09.ArduinoDataReceiver import DeviceData_Object
import time
import logging
import threading

class DevicePerformanceMonitor(threading.Thread):
    
    def __init__(self, count=1000):
        
        threading.Thread.__init__(self)  # initializing thread function
        self.count = count
        self.x = memutil()  # creating memutil instance#
        logging.info("Memory utilization Instance Created")
        self.y = cpuutil()  # creating cpuutil instance#
        logging.info("CPU utilization Instance Created")
        logging.info("SPA Instance Created")
        
    def run(self):
        
        while DevicePerformanceMonitor.is_alive(self):
            cpuData = "CPU Utilization = " + str(self.x.getSensorData()) 
            DeviceData_Object.setCpu_Util(self.x.getSensorData())
            memData = "Memory Utilization = " + str(self.y.getSensorData())
            DeviceData_Object.setMem_Util(self.y.getSensorData())
            logging.info(cpuData + "%")
            logging.info(memData + "%")
            time.sleep(5)  # Calling Thread Every 3 seconds  
            self.count -= 1  # Decrementing count call by 1            
            if self.count == 0:
                return  # stopping thread after executing 'N' times
          
