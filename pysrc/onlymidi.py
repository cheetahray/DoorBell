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
import xlsxwriter

mid = MidiFile('C:\\Windows.old\\Users\\Ray\\Music\\Shanghai\\newyear.mid')
debug = True        #Boolean for on/off our debug print 
isplay = False      #Boolean to judge whether the midi is playing


class Tests(unittest.TestCase):
    def test_0(self):   #Test play midi file
        play_midi();
        
def play_midi():
    global isplay
    global myshift
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()
    f = [[],[],[],[]]
    for i in range(127):
        f[0].append(0)
        worksheet.write(i, 0, 0)
        f[1].append(0)
        worksheet.write(i, 1, 0)
        f[2].append(0)
        worksheet.write(i, 2, 0)
        f[3].append(0)
        worksheet.write(i, 3, 0)
    for message in mid.play():  #Next note from midi in this moment
        isplay = False          #To avoid duplicate doorbell button press during midi play
        if debug:
            print(message)
        if 'note_on' == message.type :
            if 0 != message.velocity :
                if 0 == message.channel:
                    f[0][message.note] = f[0][message.note] + 1
                    worksheet.write(message.note, 0, f[0][message.note])
                elif 1 == message.channel:
                    f[1][message.note] = f[1][message.note] + 1
                    worksheet.write(message.note, 1, f[1][message.note])
                elif 2 == message.channel:
                    f[2][message.note] = f[2][message.note] + 1
                    worksheet.write(message.note, 2, f[2][message.note])
                elif 3 == message.channel:
                    f[3][message.note] = f[3][message.note] + 1
                    worksheet.write(message.note, 3, f[3][message.note])
    workbook.close()
    
try:
                    #Register the door bell button GPIO input call back function
    if '__main__' == __name__ :
        midi_suite = unittest.TestSuite()   #Add play midi test function
        all_suite = unittest.TestSuite()
        midi_suite.addTest(Tests("test_0"))
        all_suite.addTest(midi_suite)
        unittest.TextTestRunner(verbosity=1).run(all_suite)
    
    while True:
        if isplay:
            if debug:
                print isplay 
            play_midi()
        else:
            time.sleep(1)

except KeyboardInterrupt:
    print "Cleaning up the GPIO" 

