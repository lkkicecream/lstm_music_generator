import mido
import pretty_midi
from music21 import *

# we create the music21 Bottom Part, and do this explicitly, one object at a time.

n1 = note.Note('e4')
n1.duration.type = 'whole'
n2 = note.Note('d4')
n2.duration.type = 'whole'
m1 = stream.Measure()
m2 = stream.Measure()
m1.append(n1)
m2.append(n2)
partLower = stream.Part()
partLower.append(m1)
partLower.append(m2)
import music21
import random

sta = 0
end = 5000

timeon = 0
def add(notesarr, inside):
    global sta
    global end


    note = [0 for _ in range(12)]
    num = 0
    for i in range(len(notesarr)):
        note[notesarr[i]] = note[notesarr[i]] + 1


    mid = mido.MidiFile('test.mid')

    track = mido.MidiTrack()

    mid.tracks.append(track)

    track.append(mido.Message('note_on', note=inside.pitch-12, velocity=90, time=sta))
    track.append(mido.Message('note_off', note=inside.pitch-12, velocity=90, time=end))
    sta = sta + 3000
    end = end + 3000

    #print(note)


    mid.save('test.mid')
    return(note)

    #timeoff = timeon+1

    #print(timeon, timeoff)
def bass(inside):
    mid = pretty_midi.PrettyMIDI('test.mid')
    mid2 = mido.MidiFile()
    track = mido.MidiTrack()
    mid2.tracks.append(track)
    inside.pitch = inside.pitch-12
    track.append(mido.Message('note_on', note=inside.pitch, velocity=90, time=int(inside.start*1000)))
    track.append(pretty_midi.Note(90, inside.pitch, inside.start, inside.end))
    mid2.save('test2.mid')

