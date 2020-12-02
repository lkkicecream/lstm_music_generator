import music21
from sys import argv
import os
import glob
import re
import musicTheory

class NotMidFile(Exception):
    pass

usage =\
'''
Usage:
    addTrack.py <source_midi_file.mid> [output_midi_file.mid]
'''

# beats pre measure
b = 4
quarterLength = 2

def sort_note(notes):
    if len(notes) <= 1:
        return notes
    
    pivot = notes.pop(0)
    larger = [note for note in notes if note.offset >= pivot.offset]
    smaller = [note for note in notes if note.offset < pivot.offset]
    return sort_note(smaller) + [pivot] + sort_note(larger)

def addTrack(midi_file, outputName='./output.mid', addRhythm:bool=False):
    midi_file = music21.converter.parse(midi_file)
    
    # 將單旋律的所有音符分離出來
    melody = [element for element in midi_file.recurse() if isinstance(element, music21.note.Note) or isinstance(element, music21.note.Rest) or isinstance(element, music21.chord.Chord)]
    melody = sort_note(melody)
    for note in melody:
        if isinstance(note, music21.note.Note):
            note = music21.note.Note(note.nameWithOctave)
        else:
            note = music21.note.Rest(quarterLength = 0.5)

    # 判斷調性
    key = music21.analysis.discrete.analyzeStream(music21.stream.Stream(melody), 'key')
    print(key)

    # 不在同個 loop 設長度以確保時間可以被設定
    offset = 0
    for note in melody:
        if isinstance(note, music21.chord.Chord):
            for cnote in note:
                cnote.quarterLength
        note.quarterLength = 0.5

    melody_part = music21.stream.Part(melody)
    # 增加節奏
    '''
    if addRhythm:
        rhythm = musicTheory.combineRhythm(len(melody))
        for note, beat in melody, rhythm:
            note.offset = beat
    '''

    # 為每 2 拍增加和弦
    #chords = [music21.chord.Chord(melody[i*b:i*b+b]) for i in range(len(melody) // b)]
    chords = []
    notes = []
    sum = 0
    for note in melody:
        sum += note.quarterLength
        if isinstance(note, music21.chord.Chord):
            for cNote in note.notes:
                notes.append(cNote)
        else:
            notes.append(note)
        if sum >= 2 or note == melody[-1]:
            chords.append(musicTheory.makeChord(notes, key=key, quarterLengt=2))
            sum = 0
            notes = []
        
        '''
        #getNotes = melody[i*b:i*b+b]
        getNotes = []
        for j in range(i*b, i*b+b):
            getNotes.append(music21.note.Note(melody[j].nameWithOctave))

        new_chord = music21.chord.Chord(getNotes)
        chords.append(new_chord)
        '''

    offset = 0
    for chord in chords:
        for note in chord:
            note.octave = 3
            pass
        chord.offset = offset
        offset += quarterLength
    
    chord_part = music21.stream.Part(chords)
    
    #part1 = music21.stream.Part(melody)
    #part2 = music21.stream.Part(chords)

    sc = music21.stream.Score()
    sc.insert(0, melody_part)
    sc.insert(0, chord_part)

    # 輸出檔案
    midi_stream = music21.stream.Stream(sc)
    midi_stream.write('midi', fp=outputName)
    midi_stream.show()
    print('done')
    os.system('pause')
    # make 


if __name__ == '__main__':
    try:
        if(len(argv) < 2):
            raise IndexError
        midi_files = glob.glob(argv[1])
        
        if len(midi_files) == 0:
            raise FileNotFoundError('Target file is not existed.')

        if(len(argv) == 2):
            addTrack(midi_files[0])
        else:
            addTrack(midi_files[0], outputName=argv[2])

    except IndexError as e:
        print(usage)
        
'''
    a = music21.converter.parse('./test_output.mid')
    print(a.track)
'''
