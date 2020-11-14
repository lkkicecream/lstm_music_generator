import mido
from pretty_midi import *
from addmusicV2 import *
from writemap import *
from getstart import *
import os
import numpy as np
#from music import *




def beancase(bean):
    beans = ["Si", "Do", "^Do", "Re", "^Re", "Mi", "Fa", "^Fa", "So", "^So", "La", "^La"]
    if(bean==1):
        return beans[bean]
    if(bean==2):
        return beans[bean]
    if(bean==3):
        return beans[bean]
    if (bean == 4):
        return beans[bean]
    if (bean == 5):
        return beans[bean]
    if (bean == 6):
        return beans[bean]
    if (bean == 7):
        return beans[bean]
    if (bean == 8):
        return beans[bean]
    if (bean == 9):
        return beans[bean]
    if (bean == 10):
        return beans[bean]
    if (bean == 11):
        return beans[bean]
    if (bean == 0):
        return beans[bean]

def get_note_lengths(path):
    pm = pretty_midi.PrettyMIDI(path)
    x = int(0)
    y = 0
    notesarr = []
    #time = 0
    #timeoff = 0
    arr = []
    arrtime =[]
    timeon = 0
    #f1 = open("f1.txt", "w")
    #f2 = open("f1time.txt", "w")

    for instr in pm.instruments:
        if not instr.is_drum:
            for note in instr.notes:
                Str = note.start
                End = note.end
                pitch = note.pitch
                Strx = int(Str/2)
                Endx = int((End/2))
                level = int((pitch-59)/7)
                bean = int((pitch-59) % 12)
                notesarr.append(bean)
                take = beancase(bean)
                arr.append(pitch)
                arrtime.append(Str)
                x = Strx



    #f1.write(str(arr))
    #f2.write(str(arrtime))
    #f2.close()
    #f1.close()
    writemap(arr, arrtime)
    return arr

#note = get_note_lengths('test.mid')

path = 'output.mid'
starttime = getstart(path)
restart(path, starttime)
note = get_note_lengths('test.mid')
#print(note)


