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

mid = MidiFile('song.mid')
debug = True
isplay = False
BUT_PIN = 7
BOUNCE_TIME = 200
MAG1_PIN = 11   #PL2 green
MAG2_PIN = 12   #PL3 yellow
MAG3_PIN = 13   #PL1 orange
MAG4_PIN = 15   #PL5 white
MAG5_PIN = 16   #PL7 purpal
MAG6_PIN = 18   #PL6 gray
MAG7_PIN = 22   #PL4 blue

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAG1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG2_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG3_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG4_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG5_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG6_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG7_PIN, GPIO.OUT, initial=GPIO.LOW)

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
pwm_mag7 = GPIO.PWM(MAG7_PIN, 70)
pwm_mag7.start(0)

class Tests(unittest.TestCase):
    def test_0(self):
        play_midi();
        
    def test_1(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag1.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag1.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_2(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag2.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag2.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_3(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag3.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag3.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_4(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag4.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag4.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_5(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag5.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag5.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_6(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag6.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag6.ChangeDutyCycle(100)
            time.sleep(0.5)
    
    def test_7(self):
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag7.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag7.ChangeDutyCycle(100)
            time.sleep(0.5)
    
def play_midi():
    global isplay
    for message in mid.play():
        isplay = False
        if debug:
            print(message)
        if 'note_on' == message.type :
            if 60 == message.note :
                if 0 == message.velocity :
                    pwm_mag1.ChangeDutyCycle(0)
                else :
                    pwm_mag1.ChangeDutyCycle(100)
            elif 61 == message.note :
                if 0 == message.velocity :
                    pwm_mag2.ChangeDutyCycle(0)
                else :
                    pwm_mag2.ChangeDutyCycle(100)
            elif 62 == message.note :
                if 0 == message.velocity :
                    pwm_mag3.ChangeDutyCycle(0)
                else :
                    pwm_mag3.ChangeDutyCycle(100)    
            elif 63 == message.note :
                if 0 == message.velocity :
                    pwm_mag4.ChangeDutyCycle(0)
                else :
                    pwm_mag4.ChangeDutyCycle(100)
            elif 64 == message.note :
                if 0 == message.velocity :
                    pwm_mag5.ChangeDutyCycle(0)
                else :
                    pwm_mag5.ChangeDutyCycle(100)
            elif 65 == message.note :
                if 0 == message.velocity :
                    pwm_mag6.ChangeDutyCycle(0)
                else :
                    pwm_mag6.ChangeDutyCycle(100)
            elif 66 == message.note :
                if 0 == message.velocity :
                    pwm_mag7.ChangeDutyCycle(0)
                else :
                    pwm_mag7.ChangeDutyCycle(100)
        elif 'note_off' == message.type :
            if 60 == message.note :
                pwm_mag1.ChangeDutyCycle(0)
            elif 61 == message.note :
                pwm_mag2.ChangeDutyCycle(0)
            elif 62 == message.note :
                pwm_mag3.ChangeDutyCycle(0)    
            elif 63 == message.note :
                pwm_mag4.ChangeDutyCycle(0)
            elif 64 == message.note :
                pwm_mag5.ChangeDutyCycle(0)
            elif 65 == message.note :
                pwm_mag6.ChangeDutyCycle(0)
            elif 66 == message.note :
                pwm_mag7.ChangeDutyCycle(0)
                
def callback_function(channel):
    global isplay
    isplay = True
    
try:
    GPIO.add_event_detect(BUT_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)

    if '__main__' == __name__ :
        midi_suite = unittest.TestSuite()
        _1st_suite = unittest.TestSuite()
        _2st_suite = unittest.TestSuite()
        _3st_suite = unittest.TestSuite()
        _4st_suite = unittest.TestSuite()
        _5st_suite = unittest.TestSuite()
        _6st_suite = unittest.TestSuite()
        _7st_suite = unittest.TestSuite()
        all_suite = unittest.TestSuite()
        midi_suite.addTest(Tests("test_0"))
        _1st_suite.addTest(Tests("test_1"))
        _2st_suite.addTest(Tests("test_2"))
        _3st_suite.addTest(Tests("test_3"))
        _4st_suite.addTest(Tests("test_4"))
        _5st_suite.addTest(Tests("test_5"))
        _6st_suite.addTest(Tests("test_6"))
        _7st_suite.addTest(Tests("test_7"))
        all_suite.addTest(_1st_suite)
        all_suite.addTest(_2st_suite)
        all_suite.addTest(_3st_suite)
        all_suite.addTest(_4st_suite)
        all_suite.addTest(_5st_suite)
        all_suite.addTest(_6st_suite)
        all_suite.addTest(_7st_suite)
        #unittest.TextTestRunner(verbosity=1).run(midi_suite)
    
    while True:
        if isplay:
            if debug:
                print isplay 
            play_midi()

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
    GPIO.cleanup()

