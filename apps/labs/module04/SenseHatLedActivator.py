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
************************************************ Module Description********************************************************
* When an actuation is triggered by TempActuatorAdaptor class module, this class creates an instance of SenseHat library
* It has separate functions to turn on Red LED & Blue LED which uses .clear() function of sense hat library
***************************************************************************************************************************
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
    Public function to make Sense Hat LED'S glow RED colour
    '''

    def show_i2c_LED(self, i2c_humidity_value):
        text_colour = [0, 0, 0]
        back_colour = [255, 255, 255]
        x = str(i2c_humidity_value)
        self.led_glow.show_message(x, 0.1, text_colour, back_colour)
    '''
    Public function to make Sense Hat LED'S glow BLUE colour
    '''    

    def show_api_LED(self, api_humidity_value):    
        text_colour = [0, 0, 0]
        back_colour = [255, 0, 0]
        y = str(api_humidity_value)
        self.led_glow.show_message(y, 0.1, text_colour, back_colour)
    '''
    Default_LED colour (Pale White) when setBLUE or setRED function is not called
    '''

    
        
