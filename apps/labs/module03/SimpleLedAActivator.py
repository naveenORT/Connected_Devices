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
led_glow = SenseHat()
class SimpleLedActivator():
    rate_in_sec = ''
    on_led = ''
    count = 2    

    def __init__(self, time):
        self.rate_in_sec = time
        self.on_led = True
    
    def setRED(self):
        
            r = [255,0,0]
            w = [255,255,255]
            led_glow.show_letter("R")    
            time.sleep(1.5) 
            '''       
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
            self.led_glow.set_pixels(creeper_pixels) '''        
            return
        
    def setBLUE(self):    
            
            b = [0,0,255]
            w = [255,255,255]
            led_glow.show_message("L")
            time.sleep(1.5)
            '''
            bl = (0, 0, 255)  # rreen
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
            self.led_glow.set_pixels(creeper_pixels) '''                                          
            return
        