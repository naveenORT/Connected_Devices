'''
Created on Feb 15, 2020
@author: Naveen Rajendran
'''
from time import sleep
import threading
# This next import is why we need the RPi.rPIO proxy class
from sense_hat import SenseHat
import logging
import time

'''
* When an actuation is triggered by MultiActuatorAdaptor class module, this class creates an instance of SenseHat library
* It has separate functions to turn on Blue LED message for humidity_api_sensor_data  & Green LED message for humidity_i2c_sensor_data 
'''


class SimpleLedActivator():
    rate_in_sec = ''
    on_led = ''
    count = 2    
    '''
    Class constructor function helps to set status of LED 'on' & create instance of SenseHat library class
    '''

    def __init__(self, time):
        self.rate_in_sec = time
        self.on_led = True
        self.led_glow = SenseHat()  # Creating sense_hat object

    '''
    Public function to make Sense Hat LED'S show i2c humidity value in green colour
    '''

    def show_i2c_LED(self, i2c_humidity_value):
        text_colour = [0, 255, 0]
        back_colour = [0, 0, 0]
        x = round(i2c_humidity_value, 1)
        self.led_glow.show_message(str(x), 0.04, text_colour, back_colour)
        self.set_actuation_completion(True)
        logging.info("Successfully Actuated")
        
    '''
    Public function to make Sense Hat LED'S show api humidity value in blue colour
    '''    

    def show_api_LED(self, api_humidity_value):    
        text_colour = [0, 0, 255]
        back_colour = [0, 0, 0]
        y = round(api_humidity_value, 1)
        #self.led_glow.show_message(str(y), 0.04, text_colour, back_colour)
        self.set_actuation_completion(True)
        logging.info("Successfully Actuated")

    '''
    Standard setter function to set actuation_status
    Input: True or False (Boolean)
    '''

    def set_actuation_completion(self, invalue):
        self.status_of_actuation = invalue

    '''
    Standard getter function to get status_of_actuation
    Output: True or False (Boolean)
    '''

    def get_actuation_completion(self):
        return self.status_of_actuation
