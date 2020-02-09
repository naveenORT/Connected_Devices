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

class SimpleLedActivator():
    rate_in_sec = ''
    on_led = ''
    count = 2    

    def __init__(self, time):
        self.rate_in_sec = time
        self.on_led = True
        self.led_glow = SenseHat()
    
    def setRED(self):
        
        
        r = (255, 0, 0)  # rreen
        b = (0, 0, 0)  # Black    
        # Set up where each colour will display
        creeper_pixels = [
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, b, b, r, r, b, b, r,
            r, b, b, r, r, b, b, r,
            r, r, r, b, b, r, r, r,
            r, r, b, b, b, b, r, r,
            r, r, b, b, b, b, r, r,
            r, r, b, r, r, b, r, r
        ]
        # Display these colours on the LED matrix
        self.led_glow.set_pixels(creeper_pixels)         
        time.sleep(1.5)
        return
        
    def setBLUE(self):    
                    
        bl = (0, 0, 255)  # green
        b = (0, 0, 0)  # Black
        # Set up where each colour will display
        creeper_pixels = [
            bl, bl, bl, bl, bl, bl, bl, bl,
            bl, bl, bl, bl, bl, bl, bl, bl,
            bl, b, b, bl, bl, b, b, bl,
            bl, b, b, bl, bl, b, b, bl,
            bl, bl, bl, b, b, bl, bl, bl,
            bl, bl, b, b, b, b, bl, bl,
            bl, bl, b, b, b, b, bl, bl,
            bl, bl, b, bl, bl, b, bl, bl
        ]
        # Display these colours on the LED matrix
        self.led_glow.set_pixels(creeper_pixels)                                           
        time.sleep(1.5)
        return

    def default_led(self):
        self.led_glow.clear((0,0,0))
        return