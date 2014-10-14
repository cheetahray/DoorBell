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
ifplay = False
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
        isplay = False
        if 'note_on' == message.type :
            if 60 == message.note :
                if 0 == message.velocity :
                    pwm_mag0.ChangeDutyCycle(0)
                else :
                    pwm_mag0.ChangeDutyCycle(100)
            elif 61 == message.note :
                if 0 == message.velocity :
                    pwm_mag1.ChangeDutyCycle(0)
                else :
                    pwm_mag1.ChangeDutyCycle(100)
            elif 62 == message.note :
                if 0 == message.velocity :
                    pwm_mag2.ChangeDutyCycle(0)
                else :
                    pwm_mag2.ChangeDutyCycle(100)    
            elif 63 == message.note :
                if 0 == message.velocity :
                    pwm_mag3.ChangeDutyCycle(0)
                else :
                    pwm_mag3.ChangeDutyCycle(100)
            elif 64 == message.note :
                if 0 == message.velocity :
                    pwm_mag4.ChangeDutyCycle(0)
                else :
                    pwm_mag4.ChangeDutyCycle(100)
            elif 65 == message.note :
                if 0 == message.velocity :
                    pwm_mag5.ChangeDutyCycle(0)
                else :
                    pwm_mag5.ChangeDutyCycle(100)
            elif 66 == message.note :
                if 0 == message.velocity :
                    pwm_mag6.ChangeDutyCycle(0)
                else :
                    pwm_mag6.ChangeDutyCycle(100)
        elif 'note_off' == message.type :
            if 60 == message.note :
                pwm_mag0.ChangeDutyCycle(0)
            elif 61 == message.note :
                pwm_mag1.ChangeDutyCycle(0)
            elif 62 == message.note :
                pwm_mag2.ChangeDutyCycle(0)    
            elif 63 == message.note :
                pwm_mag3.ChangeDutyCycle(0)
            elif 64 == message.note :
                pwm_mag4.ChangeDutyCycle(0)
            elif 65 == message.note :
                pwm_mag5.ChangeDutyCycle(0)
            elif 66 == message.note :
                pwm_mag6.ChangeDutyCycle(0)
                
def callback_function(channel):
    isplay = True
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

    if '__main__' == __name__ :
        unittest.main()
    
    while True:
        if isplay == True
            play_midi()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
    GPIO.cleanup()



