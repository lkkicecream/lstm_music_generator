import mido
import random


timeon = 0
def add(notesarr,timeon,  timeoff):

    note = [0 for _ in range(12)]
    num = 0
    for i in range(len(notesarr)):
        note[notesarr[i]] = note[notesarr[i]] + 1



    print(note)
    '''
    mid = mido.MidiFile('test.mid')

    track = mido.MidiTrack()

    mid.tracks.append(track)

    track.append(mido.Message('note_on', note=75, velocity=96, time=timeon))
    track.append(mido.Message('note_off', note=75, velocity=96, time=timeoff))

    

    mid.save('test.mid')
    '''
    #timeoff = timeon+1

    #print(timeon, timeoff)
