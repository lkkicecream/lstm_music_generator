import mido
from pretty_midi import *
from addmusic import *
from writemap import *
from getstart import *
from whichkey import *
import os
import numpy as np
#from music import *
from pathlib import Path


#當初用來確認傳入資料為什麼音
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

#分出每個小節
def get_note_Done(path, noterange):
    pm = pretty_midi.PrettyMIDI(path)
    x = int(0) #記錄第幾小節
    y = 0 #紀錄上一個小節的時間點
    notesarr = [] #紀錄音符
    arr = [] #紀錄Do Re Mi
    arrtime =[] #紀錄每個音的開始時間

    for instr in pm.instruments:
        if not instr.is_drum:
            for note in instr.notes:
                Str = note.start
                pitch = note.pitch
                Strx = int(Str/2) #一小節有兩拍，所以除2
                bean = int((pitch-59) % 12) #紀錄是哪個音
                notesarr.append(bean)
                arr.append(pitch)
                arrtime.append(Str)
                x = Strx


    writemap(arr, arrtime,noterange) #呼叫writemap
    return arr

