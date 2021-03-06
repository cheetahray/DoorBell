#!/usr/bin/python
#+-+-+-+-+-+-+
#|d|a|c|.|t|w|
#+-+-+-+-+-+-+
#
# doorbell.py
# Read a button input to trigger midi play then do some GPIO outputs.
#
# Author : Digital Art Center, Taipei.
# Date   : 11/18/2014

import RPi.GPIO as GPIO
import time
import unittest
from mido import MidiFile

mid = MidiFile('/home/pi/DoorBell/pysrc/song.mid')
debug = True        #Boolean for on/off our debug print 
#isplay = False      #Boolean to judge whether the midi is playing
myshift = 12
BUT_CNT = 0
BUT_PIN = 7         #Doorbell button GPIO input pin number
BOUNCE_TIME = 200   #GPIO input delay time
MAG1_PIN = 11       #GPIO pin number output to magnet PL1 red
MAG2_PIN = 12       #GPIO pin number output to magnet PL2 orange
MAG3_PIN = 13       #GPIO pin number output to magnet PL3 yellow
MAG4_PIN = 15       #GPIO pin number output to magnet PL4 green
MAG5_PIN = 16       #GPIO pin number output to magnet PL5 blue
MAG6_PIN = 18       #GPIO pin number output to magnet PL6 
MAG7_PIN = 22       #GPIO pin number output to magnet PL7 purple

GPIO.setmode(GPIO.BOARD)    #Set GPIO input/output
GPIO.setup(BUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(MAG1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG2_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG3_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG4_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG5_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG6_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MAG7_PIN, GPIO.OUT, initial=GPIO.LOW)

pwm_mag1 = GPIO.PWM(MAG1_PIN, 70)   #Initial PWM
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
    def test_0(self):   #Test play midi file
        play_midi();
        
    def test_1(self):   #Test 1st magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag1.ChangeDutyCycle(100)
            time.sleep(0.3)
            pwm_mag1.ChangeDutyCycle(0)
            time.sleep(0.5)
        
    def test_2(self):   #Test 2nd magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag2.ChangeDutyCycle(100)
            time.sleep(0.5)
            pwm_mag2.ChangeDutyCycle(0)
            time.sleep(0.5)
        
    def test_3(self):   #Test 3rd magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag3.ChangeDutyCycle(100)
            time.sleep(0.5)
            pwm_mag3.ChangeDutyCycle(0)
            time.sleep(0.5)
        
    def test_4(self):   #Test 4th magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag4.ChangeDutyCycle(100)
            time.sleep(0.5)
            pwm_mag4.ChangeDutyCycle(0)
            time.sleep(0.5)
        
    def test_5(self):   #Test 5th magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag5.ChangeDutyCycle(100)
            time.sleep(0.5)
            pwm_mag5.ChangeDutyCycle(0)
            time.sleep(0.5)
        
    def test_6(self):   #Test 6th magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag6.ChangeDutyCycle(100)
            time.sleep(0.5)
            pwm_mag6.ChangeDutyCycle(0)
            time.sleep(0.5)
    
    def test_7(self):   #Test 7th magnet for 10 times
        for i in range(1,1):
            if debug:
                print(i)
            pwm_mag7.ChangeDutyCycle(100)
            time.sleep(0.5)
            pwm_mag7.ChangeDutyCycle(0)
            time.sleep(0.5)
    
    def test_8(self):   #Test 7th magnet for 10 times
        pwm_mag1.ChangeDutyCycle(100)
        time.sleep(0.1)
        pwm_mag1.ChangeDutyCycle(0)
        time.sleep(0.1)
        pwm_mag2.ChangeDutyCycle(100)
        time.sleep(0.1)
        pwm_mag2.ChangeDutyCycle(0)
        time.sleep(0.1)
        pwm_mag4.ChangeDutyCycle(100)
        time.sleep(0.1)
        pwm_mag4.ChangeDutyCycle(0)
        time.sleep(0.1)
        pwm_mag5.ChangeDutyCycle(100)
        time.sleep(0.1)
        pwm_mag5.ChangeDutyCycle(0)
        time.sleep(0.1)
        pwm_mag6.ChangeDutyCycle(100)
        time.sleep(0.1)
        pwm_mag6.ChangeDutyCycle(0)
        time.sleep(0.1)
        
def play_midi():
    #global isplay
    global myshift
    global BUT_CNT
    for message in mid.play():  #Next note from midi in this moment
        #isplay = False          #To avoid duplicate doorbell button press during midi play
        if 'note_on' == message.type :
            if debug:
                print('%d ' % message.note),
            if (60-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag1.ChangeDutyCycle(0)     #Do off
                else :
                    pwm_mag1.ChangeDutyCycle(100)   #Do on
            elif (62-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag2.ChangeDutyCycle(0)     #Re off
                else :
                    pwm_mag2.ChangeDutyCycle(100)   #Re on
            elif (64-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag4.ChangeDutyCycle(0)     #Mi off
                else :
                    pwm_mag4.ChangeDutyCycle(100)   #Mi on
            elif (65-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag5.ChangeDutyCycle(0)     #Fa off
                else :
                    pwm_mag5.ChangeDutyCycle(100)   #Fa on
            elif (67-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag6.ChangeDutyCycle(0)     #So off
                else :
                    pwm_mag6.ChangeDutyCycle(100)   #So on
            elif (69-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag3.ChangeDutyCycle(0)     #La off
                else :
                    pwm_mag3.ChangeDutyCycle(100)   #La on
            elif (71-myshift) == message.note :
                if 0 == message.velocity :
                    pwm_mag7.ChangeDutyCycle(0)     #Ti off
                else :
                    pwm_mag7.ChangeDutyCycle(100)   #Ti on
        elif 'note_off' == message.type :
            if (60-myshift) == message.note :
                pwm_mag1.ChangeDutyCycle(0)         #Do off
            elif (62-myshift) == message.note :
                pwm_mag2.ChangeDutyCycle(0)         #Re off
            elif (64-myshift) == message.note :
                pwm_mag4.ChangeDutyCycle(0)         #Mi off
            elif (65-myshift) == message.note :
                pwm_mag5.ChangeDutyCycle(0)         #Fa off
            elif (67-myshift) == message.note :
                pwm_mag6.ChangeDutyCycle(0)         #So off
            elif (69-myshift) == message.note :
                pwm_mag3.ChangeDutyCycle(0)         #La off
            elif (71-myshift) == message.note :
                pwm_mag7.ChangeDutyCycle(0)         #Ti off
    BUT_CNT = 0
                
#def callback_function(channel):
    #global isplay
    #isplay = True   #Switch on the boolean of midi play 

try:
    #GPIO.add_event_detect(BUT_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)
                    #Register the door bell button GPIO input call back function

    if '__main__' == __name__ :
        midi_suite = unittest.TestSuite()   #Add play midi test function
        _1st_suite = unittest.TestSuite()   #Add 1st magnet test function
        _2st_suite = unittest.TestSuite()   #Add 2nd magnet test function
        _3st_suite = unittest.TestSuite()   #Add 3rd magnet test function
        _4st_suite = unittest.TestSuite()   #Add 4th magnet test function
        _5st_suite = unittest.TestSuite()   #Add 5th magnet test function
        _6st_suite = unittest.TestSuite()   #Add 6th magnet test function
        _7st_suite = unittest.TestSuite()   #Add 7th magnet test function
        _8st_suite = unittest.TestSuite()   #Add 7th magnet test function
        all_suite = unittest.TestSuite()
        midi_suite.addTest(Tests("test_0"))
        _1st_suite.addTest(Tests("test_1"))
        _2st_suite.addTest(Tests("test_2"))
        _3st_suite.addTest(Tests("test_3"))
        _4st_suite.addTest(Tests("test_4"))
        _5st_suite.addTest(Tests("test_5"))
        _6st_suite.addTest(Tests("test_6"))
        _7st_suite.addTest(Tests("test_7"))
        _8st_suite.addTest(Tests("test_8"))
        all_suite.addTest(_1st_suite)
        all_suite.addTest(_2st_suite)
        all_suite.addTest(_3st_suite)
        all_suite.addTest(_4st_suite)
        all_suite.addTest(_5st_suite)
        all_suite.addTest(_6st_suite)
        all_suite.addTest(_7st_suite)
        #unittest.TextTestRunner(verbosity=1).run(_8st_suite)
    
    while True:
        if BUT_CNT > 300:
            if debug:
                print BUT_CNT 
            play_midi()
        elif GPIO.input(BUT_PIN) == GPIO.HIGH :
            BUT_CNT = BUT_CNT + 1
        else:
            time.sleep(0.333)

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
    GPIO.cleanup()

