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

mid = MidiFile('song.mid')
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
    f = []
    for i in range(127):
        f.append(0)
        worksheet.write(i, 0, 0)
    for message in mid.play():  #Next note from midi in this moment
        isplay = False          #To avoid duplicate doorbell button press during midi play
        if debug:
            print(message)
        if 'note_on' == message.type :
            if 0 != message.velocity :
                f[message.note] = f[message.note] + 1
                worksheet.write(message.note, 0, f[message.note])
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

