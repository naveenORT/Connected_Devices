'''
Created on Jan 14, 2020
@author: Naveen Rajendran
'''
from labs.module01.SystemMemUtilTask import memutil
from labs.module01.SystemCpuUtilTask import cpuutil
import time
import logging
import threading


class SystemPerformanceAdaptor(threading.Thread): 

    def __init__(self, count):
        
        threading.Thread.__init__(self)  # initializing thread function
        self.count = count
        self.x = memutil()  # creating memutil instance#
        logging.info("Memory utilization Instance Created")
        self.y = cpuutil()  # creating cpuutil instance#
        logging.info("CPU utilization Instance Created")
        logging.info("SPA Instance Created")
        
    def run(self):
        
        while SystemPerformanceAdaptor.is_alive(self):
            cpuData = "CPU Utilization = " + str(self.x.getSensorData()) 
            memData = "Memory Utilization = " + str(self.y.getSensorData())
            logging.info(cpuData + "%")
            logging.info(memData + "%")
            time.sleep(3)  # Calling Thread Every 3 seconds  
            self.count -= 1  # Decrementing count call by 1
            
            if self.count == 0:
                return  # stopping thread after executing 'N' times
          
