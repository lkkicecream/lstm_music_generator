import music21
import json
import random
import math
import numpy as np


rhythm = []
chord = {}

with open('./musicTheory/rythem.json','r') as _:
    rythem = json.loads(_.read())

with open('./musicTheory/chord.json','r') as _:
    chord = json.loads(_.read())

def combineRhythm(beats:int=1):
    combList = []
    while beats > 0:
        randList1 = random.choice(rythem)
        if len(randList1)==0:
            continue
        randList2 = random.choice(randList1)
        combList = combList + randList2
        beats -= rythem.index(randList1)
    return combList

def makeChord(notes, root=music21.note.Note('C'), quarterLengt=4):
    countNote = np.zeros(12, dtype=int)
    major = [(i in chord['Maj']) for i in range(12)]
    minor = [(i in chord['Min']) for i in range(12)]
    currChord = None
    max = 0
    
    for note in notes:
        countNote[int(note.pitch.ps)%12] += 1
    #print(countNote)
    # 利用 mask 做比對
    
    for _ in range(12):
        # 大和弦
        sum = 0
        for i in range(12):
            if major[i]:
                sum += countNote[i]
        if sum > max:
            max = sum
            currChord = major[:]
        major = major[-1:] + major[:-1]
        
        # 小和弦
        sum = 0
        for i in range(12):
            if minor[i]:
                sum += countNote[i]
        if sum > max:
            max = sum
            currChord = minor[:]
        minor = minor[-1:] + minor[:-1]
    
    newChord = music21.chord.Chord([music21.note.Note(i) for i in range(12) if currChord[i] == True], quarterLength=quarterLengt)
    return newChord

'''
note = music21.note.Note('C')
print(note.pitch)
print(int(note.pitch.ps))
'''