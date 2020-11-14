from pretty_midi import *
import mido

def getstart(path):
    pm = pretty_midi.PrettyMIDI(path)
    for instr in pm.instruments:
        for note in instr.notes:
            starttime = note.start
            return starttime

def restart(path,subtime):

    pm = pretty_midi.PrettyMIDI(path)
    #subtime = pm.instruments.notes[0].timeon

    for instr in pm.instruments:
        for note in instr.notes:
            st = note.start - subtime
            en = note.end - subtime
            note.start = st
            note.end = en

    pm.write('test.mid')

#restart('1111.mid',0.5)
