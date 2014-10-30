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
from apscheduler.schedulers.background import BackgroundScheduler

mid = MidiFile('song.mid')
debug = True        #Boolean for on/off our debug print 
isplay = False      #Boolean to judge whether the midi is playing
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
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag1.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag1.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_2(self):   #Test 2nd magnet for 10 times
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag2.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag2.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_3(self):   #Test 3rd magnet for 10 times
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag3.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag3.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_4(self):   #Test 4th magnet for 10 times
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag4.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag4.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_5(self):   #Test 5th magnet for 10 times
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag5.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag5.ChangeDutyCycle(100)
            time.sleep(0.5)
        
    def test_6(self):   #Test 6th magnet for 10 times
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag6.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag6.ChangeDutyCycle(100)
            time.sleep(0.5)
    
    def test_7(self):   #Test 7th magnet for 10 times
        for i in range(1,10):
            if debug:
                print(i)
            pwm_mag7.ChangeDutyCycle(0)
            time.sleep(0.5)
            pwm_mag7.ChangeDutyCycle(100)
            time.sleep(0.5)
    
def play_midi():
    global isplay
    global job1
    global job2
    global job3
    global job4
    global job5
    global job6
    global job7
    global isorgan
    for message in mid.play():  #Next note from midi in this moment
        isplay = False          #To avoid duplicate doorbell button press during midi play
        #if debug:
            #print(message)
        if 'note_on' == message.type :
            if 60 == message.note :
                if 0 == message.velocity :
                    pwm_mag1.ChangeDutyCycle(0)     #Do off
                else :
                    if False == isorgan:
                        job1.resume()
                    pwm_mag1.ChangeDutyCycle(100)   #Do on
            elif 61 == message.note :
                if 0 == message.velocity :
                    pwm_mag2.ChangeDutyCycle(0)     #Re off
                else :
                    if False == isorgan:
                        job2.resume()
                    pwm_mag2.ChangeDutyCycle(100)   #Re on
            elif 62 == message.note :
                if 0 == message.velocity :
                    pwm_mag3.ChangeDutyCycle(0)     #Mi off
                else :
                    if False == isorgan:
                        job3.resume()
                    pwm_mag3.ChangeDutyCycle(100)   #Mi on
            elif 63 == message.note :
                if 0 == message.velocity :
                    pwm_mag4.ChangeDutyCycle(0)     #Fa off
                else :
                    if False == isorgan:
                        job4.resume()
                    pwm_mag4.ChangeDutyCycle(100)   #Fa on
            elif 64 == message.note :
                if 0 == message.velocity :
                    pwm_mag5.ChangeDutyCycle(0)     #So off
                else :
                    if False == isorgan:
                        job5.resume()
                    pwm_mag5.ChangeDutyCycle(100)   #So on
            elif 65 == message.note :
                if 0 == message.velocity :
                    pwm_mag6.ChangeDutyCycle(0)     #La off
                else :
                    if False == isorgan:
                        job6.resume()
                    pwm_mag6.ChangeDutyCycle(100)   #La on
            elif 66 == message.note :
                if 0 == message.velocity :
                    pwm_mag7.ChangeDutyCycle(0)     #Ti off
                else :
                    if False == isorgan:
                        job7.resume()
                    pwm_mag7.ChangeDutyCycle(100)   #Ti on
        elif 'note_off' == message.type :
            if 60 == message.note :
                pwm_mag1.ChangeDutyCycle(0)         #Do off
            elif 61 == message.note :
                pwm_mag2.ChangeDutyCycle(0)         #Re off
            elif 62 == message.note :
                pwm_mag3.ChangeDutyCycle(0)         #Mi off
            elif 63 == message.note :
                pwm_mag4.ChangeDutyCycle(0)         #Fa off
            elif 64 == message.note :
                pwm_mag5.ChangeDutyCycle(0)         #So off
            elif 65 == message.note :
                pwm_mag6.ChangeDutyCycle(0)         #La off
            elif 66 == message.note :
                pwm_mag7.ChangeDutyCycle(0)         #Ti off
                
def callback_function(channel):
    global isplay
    isplay = True   #Switch on the boolean of midi play 

def do_job():
    global job1
    if debug:
        print "Every do seconds"
    pwm_mag1.ChangeDutyCycle(0)
    job1.pause()

def re_job():
    global job2
    if debug:
        print "Every re seconds"
    pwm_mag2.ChangeDutyCycle(0)
    job2.pause()

def mi_job():
    global job3
    if debug:
        print "Every mi seconds"
    pwm_mag3.ChangeDutyCycle(0)
    job3.pause()

def fa_job():
    global job4
    if debug:
        print "Every fa seconds"
    pwm_mag4.ChangeDutyCycle(0)
    job4.pause()

def so_job():
    global job5
    if debug:
        print "Every so seconds"
    pwm_mag5.ChangeDutyCycle(0)
    job5.pause()

def la_job():
    global job6
    if debug:
        print "Every la seconds"
    pwm_mag6.ChangeDutyCycle(0)
    job6.pause()

def ti_job():
    global job7
    if debug:
        print "Every ti seconds"
    pwm_mag7.ChangeDutyCycle(0)
    job7.pause()

sched = BackgroundScheduler()
isorgan = False
job1 = sched.add_job(do_job, 'interval', seconds = 0.1)
job2 = sched.add_job(re_job, 'interval', seconds = 0.1)
job3 = sched.add_job(mi_job, 'interval', seconds = 0.1)
job4 = sched.add_job(fa_job, 'interval', seconds = 0.1)
job5 = sched.add_job(so_job, 'interval', seconds = 0.1)
job6 = sched.add_job(la_job, 'interval', seconds = 0.1)
job7 = sched.add_job(ti_job, 'interval', seconds = 0.1)
  
try:
    GPIO.add_event_detect(BUT_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)
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
    
    sched.start()
    job1.pause()
    job2.pause()
    job3.pause()
    job4.pause()
    job5.pause()
    job6.pause()
    job7.pause()
    
    while True:
        if isplay:
            if debug:
                print isplay 
            play_midi()
            job1.pause()
            job2.pause()
            job3.pause()
            job4.pause()
            job5.pause()
            job6.pause()
            job7.pause()
        else:
            time.sleep(1)

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 
    GPIO.cleanup()
    sched.shutdown()

