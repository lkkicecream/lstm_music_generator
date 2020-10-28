import mido
from pretty_midi import *
from addmusic import *
import os
import numpy as np
#from music import *
from getdrum import *



def beancase(bean):
    beans = ["Si","Do","^Do","Re","^Re","Mi","Fa","^Fa","So","^So","La","^La"]
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
    timeon = 0
    for instr in pm.instruments:
        if not instr.is_drum:
            for note in instr.notes:
                Str = note.start
                End = note.end
                pitch = note.pitch
                Strx = int(Str/4)
                Endx = int((End+1.25)/4)

                level = int((pitch-59)/7)
                bean = int((pitch-59) % 12)
                notesarr.append(bean)
                take = beancase(bean)
                arr.append(take)

                #print("[", level, take, "]", "(", note.start)
                if (x!=Endx and x+1 < (End+1.25)/4):
                    y = 1
                    timeoff = End
                    add(notesarr, timeon, timeoff)
                    timeon = timeoff
                    print(arr)
                    print("//////////////", x, "小節線")
                    notesarr = []
                    arr = []
                #print(note.end, ")")
                if (x!=Endx and y==0):
                    timeoff = End
                    add(notesarr,timeon, timeoff)
                    timeon = timeoff
                    print(arr)
                    print("//////////////", x, "小節線")
                    notesarr = []
                    arr = []
                x = Endx
                y = 0
    return arr
'''
def notes(path):
    notesarr = [0 for _ in range(12)]
    pm = pretty_midi.PrettyMIDI(path)
    for instr in pm.instruments:
        for note in instr.notes:
            length = note
            pitch = note.pitch
    return notes_length

mid = mido.MidiFile("outputsame.mid")
for i, track in enumerate(mid.tracks):#enumerate()：创建索引序列，索引初始为0
    print('Track {}: {}'.format(i, track.name))
    for msg in track:#每个音轨的消息遍历
        print(msg)'''
note = get_note_lengths('outputsame.mid')
#print(note)


