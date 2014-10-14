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
import unittest
from mido import MidiFile

class Tests(unittest.TestCase):
    def test_1(self):
        play_midi();
    
mid = MidiFile('song.mid')

BUT_PIN = 7
BOUNCE_TIME = 200
MAG0_PIN = 11
MAG1_PIN = 12
MAG2_PIN = 13
MAG3_PIN = 15
MAG4_PIN = 16
MAG5_PIN = 18
MAG6_PIN = 22

def play_midi():
    for message in mid.play():
        if message.type == 'note_on' :
            if message.note == 60 :
                if message.velocity == 0 :
                    pwm_mag0.ChangeDutyCycle(0)
                else :
                    pwm_mag0.ChangeDutyCycle(100)
            elif message.note == 62 :
                if(message.velocity == 0):
                    pwm_mag1.ChangeDutyCycle(0)
                else
                    pwm_mag1.ChangeDutyCycle(100)
            elif(message.note == 63):
                if(message.velocity == 0):
                    pwm_mag2.ChangeDutyCycle(0)
                else
                    pwm_mag2.ChangeDutyCycle(100)    
            elif(message.note == 64):
                if(message.velocity == 0):
                    pwm_mag3.ChangeDutyCycle(0)
                else
                    pwm_mag3.ChangeDutyCycle(100)
            elif(message.note == 65):
                if(message.velocity == 0):
                    pwm_mag4.ChangeDutyCycle(0)
                else
                    pwm_mag4.ChangeDutyCycle(100)
            elif(message.note == 66):
                if(message.velocity == 0):
                    pwm_mag5.ChangeDutyCycle(0)
                else
                    pwm_mag5.ChangeDutyCycle(100)
            elif(message.note == 67):
                if(message.velocity == 0):
                    pwm_mag6.ChangeDutyCycle(0)
                else
                    pwm_mag6.ChangeDutyCycle(100)
        elif(message.type == 'note_off'):
            if(message.note == 60):
                pwm_mag0.ChangeDutyCycle(0)
            elif(message.note == 62):
                pwm_mag1.ChangeDutyCycle(0)
            elif(message.note == 63):
                pwm_mag2.ChangeDutyCycle(0)    
            elif(message.note == 64):
                pwm_mag3.ChangeDutyCycle(0)
            elif(message.note == 65):
                pwm_mag4.ChangeDutyCycle(0)
            elif(message.note == 66):
                pwm_mag5.ChangeDutyCycle(0)
            elif(message.note == 67):
                pwm_mag6.ChangeDutyCycle(0)

def callback_function(channel):
    play_midi()
    #print "Button detected! ", time.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAG0_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG2_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG3_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG4_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG5_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG6_PIN, GPIO.OUT, initial=GPIO.LOW)

pwm_mag0 = GPIO.PWM(MAG0_PIN, 70)
pwm_mag0.start(0)
pwm_mag1 = GPIO.PWM(MAG1_PIN, 70)
pwm_mag1.start(0)
pwm_mag2 = GPIO.PWM(MAG2_PIN, 70)
pwm_mag2.start(0)
pwm_mag3 = GPIO.PWM(MAG3_PIN, 70)
pwm_mag3.start(0)
pwm_mag4 = GPIO.PWM(MAG4_PIN, 70)
pwm_mag4.start(0)
pwm_mag5 = GPIO.PWM(MAG5_PIN, 70)
pwm_mag5.start(0)
pwm_mag6 = GPIO.PWM(MAG6_PIN, 70)
pwm_mag6.start(0)

try:
    GPIO.add_event_detect(BUT_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)

    if __name__ ==  '__main__'
        unittest.main()
    
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
    GPIO.cleanup()



