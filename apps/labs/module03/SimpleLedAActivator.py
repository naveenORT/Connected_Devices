'''
Created on Feb 6, 2020
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

    def setRED(self):
       
        r = (255, 0, 0)  # rreen
        b = (0, 0, 0)  # Black    
        # Set up where each colour will display
        pixel_index = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, b, b, r, r, b, b, r,
            r, b, b, r, r, b, b, r,
            r, r, r, b, b, r, r, r,
            r, r, b, b, b, b, r, r,
            r, r, b, b, b, b, r, r,
            r, r, b, r, r, b, r, r
        ]
        self.led_glow.set_pixels(pixel_index)  # Display these colours on the LED matrix         
        time.sleep(0.5)                         
        return

    '''
    Public function to make Sense Hat LED'S glow BLUE colour
    '''    

    def setBLUE(self):    
                    
        bl = (0, 0, 255)  # green
        b = (0, 0, 0)  # Black
        # Set up where each colour will display
        pixel_index = [
            bl, bl, bl, bl, bl, bl, bl, bl,
            bl, bl, bl, bl, bl, bl, bl, bl,
            bl, b, b, bl, bl, b, b, bl,
            bl, b, b, bl, bl, b, b, bl,
            bl, bl, bl, b, b, bl, bl, bl,
            bl, bl, b, b, b, b, bl, bl,
            bl, bl, b, b, b, b, bl, bl,
            bl, bl, b, bl, bl, b, bl, bl
        ]
        self.led_glow.set_pixels(pixel_index)  # Display these colours on the LED matrix
        time.sleep(0.5)
        return

    '''
    Default_LED colour (Pale White) when setBLUE or setRED function is not called
    '''

    def default_led(self):
        self.led_glow.clear((100, 255, 175))
        return

