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

import time
import unittest
from mido import MidiFile
#import xlsxwriter
import serial

mid = MidiFile('C:\\Windows.old\\Users\\Ray\\Music\\Shanghai\\newyear.mid')
debug = True        #Boolean for on/off our debug print 
isplay = False      #Boolean to judge whether the midi is playing


class Tests(unittest.TestCase):
    def test_0(self):   #Test play midi file
        play_midi();

def checkbound(whattype, oidx):
    global ST,AT,TT,BT
    if 67 == oidx:
        oidx = 1
    if 3 == whattype:
        while 0 == BT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 2 == whattype:
        while 0 == TT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 1 == whattype:
        while 0 == AT[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    elif 0 == whattype:
        while 0 == ST[oidx]:
            if 66 == oidx:
                oidx = 1
            else:
                oidx += 1
    return oidx                
        
def play_midi():
    global isplay
    global myshift
    global port
    global boidx,toidx,aoidx,soidx
    #workbook = xlsxwriter.Workbook('demo.xlsx')
    #worksheet = workbook.add_worksheet()
    #f = []
    #for i in range(127):
        #f.append(0)
        #worksheet.write(i, 0, 0)
    for message in mid.play():  #Next note from midi in this moment
        isplay = False          #To avoid duplicate doorbell button press during midi play
        if debug:
            print(message)
        if 'note_on' == message.type :
            if 0 == message.velocity:
                if message.channel == 3:
                    if diction[3].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[3][message.note]) + "\r")
                        del diction[3][message.note]
                elif message.channel == 2:
                    if diction[2].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[2][message.note]) + "\r")
                        del diction[2][message.note]
                elif message.channel == 1:
                    if diction[1].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[1][message.note]) + "\r")
                        del diction[1][message.note]
                elif message.channel == 0:
                    if diction[0].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[0][message.note]) + "\r")
                        del diction[0][message.note]
                elif message.channel == 11:
                    if diction[7].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[7][message.note]) + "\r")
                        del diction[7][message.note]
                    if diction[11].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[11][message.note]) + "\r")
                        del diction[11][message.note]
                elif message.channel == 10:
                    if diction[6].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[6][message.note]) + "\r")
                        del diction[6][message.note]
                    if diction[10].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[10][message.note]) + "\r")
                        del diction[10][message.note]
                elif message.channel == 9:
                    if diction[5].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[5][message.note]) + "\r")
                        del diction[5][message.note]
                    if diction[9].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[9][message.note]) + "\r")
                        del diction[9][message.note]
                elif message.channel == 8:
                    if diction[4].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[4][message.note]) + "\r")
                        del diction[4][message.note]
                    if diction[8].has_key(message.note):
                        port.write("144 " + str(message.note) + " 0 " + str(diction[8][message.note]) + "\r")
                        del diction[8][message.note]
            else:
                if message.channel == 3:
                    boidx = checkbound(3,boidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(boidx) + "\r")
                    diction[3][message.note] = boidx
                    boidx += 1
                elif message.channel == 2:
                    toidx = checkbound(2,toidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(toidx) + "\r")
                    diction[2][message.note] = toidx
                    toidx += 1
                elif message.channel == 1:
                    aoidx = checkbound(1,aoidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(aoidx) + "\r")
                    diction[1][message.note] = aoidx
                    aoidx += 1
                elif message.channel == 0:
                    soidx = checkbound(0,soidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(soidx) + "\r")
                    diction[0][message.note] = soidx
                    soidx += 1
                elif message.channel == 11:
                    boidx = checkbound(3,boidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(boidx) + "\r")
                    diction[7][message.note] = boidx
                    boidx += 1
                    boidx = checkbound(3,boidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(boidx) + "\r")
                    diction[11][message.note] = boidx
                    boidx += 1
                elif message.channel == 10:
                    toidx = checkbound(2,toidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(toidx) + "\r")
                    diction[6][message.note] = toidx
                    toidx += 1
                    toidx = checkbound(2,toidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(toidx) + "\r")
                    diction[10][message.note] = toidx
                    toidx += 1
                elif message.channel == 9:
                    aoidx = checkbound(1,aoidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(aoidx) + "\r")
                    diction[5][message.note] = aoidx
                    aoidx += 1
                    aoidx = checkbound(1,aoidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(aoidx) + "\r")
                    diction[9][message.note] = aoidx
                    aoidx += 1
                elif message.channel == 8:
                    soidx = checkbound(0,soidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(soidx) + "\r")
                    diction[4][message.note] = soidx
                    soidx += 1
                    soidx = checkbound(0,soidx)
                    port.write("144 " + str(message.note) + " " + str(message.velocity) + " " + str(soidx) + "\r")
                    diction[8][message.note] = soidx
                    soidx += 1
        elif 'note_off' == message.type :
            if message.channel == 3:
                if diction[3].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[3][message.note]) + "\r")
                    del diction[3][message.note]
            elif message.channel == 2:
                if diction[2].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[2][message.note]) + "\r")
                    del diction[2][message.note]
            elif message.channel == 1:
                if diction[1].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[1][message.note]) + "\r")
                    del diction[1][message.note]
            elif message.channel == 0:
                if diction[0].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[0][message.note]) + "\r")
                    del diction[0][message.note]
            elif message.channel == 11:
                if diction[7].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[7][message.note]) + "\r")
                    del diction[7][message.note]
                if diction[11].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[11][message.note]) + "\r")
                    del diction[11][message.note]
            elif message.channel == 10:
                if diction[6].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[6][message.note]) + "\r")
                    del diction[6][message.note]
                if diction[10].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[10][message.note]) + "\r")
                    del diction[10][message.note]
            elif message.channel == 9:
                if diction[5].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[5][message.note]) + "\r")
                    del diction[5][message.note]
                if diction[9].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[9][message.note]) + "\r")
                    del diction[9][message.note]
            elif message.channel == 8:
                if diction[4].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[4][message.note]) + "\r")
                    del diction[4][message.note]
                if diction[8].has_key(message.note):
                    port.write("128 " + str(message.note) + " " + str(message.velocity) + " " + str(diction[8][message.note]) + "\r")
                    del diction[8][message.note]
                    
    port.flush()
    
ST = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
AT = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
TT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ,0 ,0 ,0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,1 ,1 ,1 ,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soidx = 1
aoidx = 1
toidx = 1
boidx = 1
diction = [{},{},{},{},{},{},{},{},{},{},{},{}]
    
port = serial.Serial("\\\\.\\COM32", baudrate=115200)
try:
    port.flushInput()
    port.flushOutput()

    
    #Register the door bell button GPIO input call back function
    if '__main__' == __name__ :
        midi_suite = unittest.TestSuite()   #Add play midi test function
        all_suite = unittest.TestSuite()
        midi_suite.addTest(Tests("test_0"))
        all_suite.addTest(midi_suite)
        unittest.TextTestRunner(verbosity=1).run(all_suite)
    else:
        whoami = "7"
        port.write("253 " + whoami + " 70\r")
        for ii in range(48,68):
            port.write("144 " + str(ii) + " 64 " + whoami + "\r")
            time.sleep(1.5)
            port.write("128 " + str(ii) + " 64 " + whoami + "\r")
        #port.flush()
    
    #while True:
    #    if isplay:
    #        if debug:
    #            print isplay 
    #        play_midi()
    #    else:
    #        time.sleep(1)

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 

