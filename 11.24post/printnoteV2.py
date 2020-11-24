import mido
from pretty_midi import *
from addmusicV2 import *
from writemap import *
from getstart import *
from whichkey import *
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

def get_note_lengths(path, noterange):
    pm = pretty_midi.PrettyMIDI(path)
    x = int(0)
    y = 0
    notesarr = []
    arr = []
    arrtime =[]

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


    writemap(arr, arrtime,noterange)
    return arr

path = 'output2.mid'


a = music21.converter.parse(path)
Key = music21.analysis.discrete.analyzeStream(a, 'key')
noterange = whichkey(Key)

starttime = getstart(path)
restart(path, starttime)
note = get_note_lengths('test.mid', noterange)


