#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pir.py
# Sense human and print message with PIR(Passive InfraRed Sensor) sensor
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

PIR_PIN = 26
BOUNCE_TIME = 200

def callback_function(channel):
        print "Motion detected! ", time.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)

        while True:
                time.sleep(1)

except KeyboardInterrupt:
        print "Cleaning up the GPIO" 
	GPIO.cleanup()



