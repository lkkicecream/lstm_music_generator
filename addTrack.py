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
    python addTrack.py <midi_file.mid>
'''

# beats pre measure
b = 4
quarterLengt = 2

def addTrack(midi_file, addRhythm:bool=False):
    midi_file = music21.converter.parse(midi_file)
    
    # 將單旋律的所有音符分離出來
    melody = [element for element in midi_file.recurse() if isinstance(element, music21.note.Note) or isinstance(element, music21.note.Rest)]
    for note in melody:
        if isinstance(note, music21.note.Note):
            note = music21.note.Note(note.nameWithOctave)
    # 不在同個 loop 設長度以確保時間可以被設定
    for note in melody:    
        if isinstance(note, music21.note.Note):
            note.quarterLength = 0.5
    print(melody[1].quarterLength)
    melody_part = music21.stream.Part(melody)
    # 增加節奏
    '''
    if addRhythm:
        rhythm = musicTheory.combineRhythm(len(melody))
        for note, beat in melody, rhythm:
            note.offset = beat
    '''

    # 為每 4 拍增加和弦
    #chords = [music21.chord.Chord(melody[i*b:i*b+b]) for i in range(len(melody) // b)]
    chords = []
    for i in range(len(melody) // b):
        sum = 0
        for j in range(i,len(melody)):
            sum += melody[j].quarterLength
            if sum >= 2:
                break
        chords.append(musicTheory.makeChord(melody[i*b:i*b+b], key=music21.key.Key('B-'), quarterLengt=2))
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
        offset += quarterLengt
        # print(chord)
    
    chord_part = music21.stream.Part(chords)
    
    #part1 = music21.stream.Part(melody)
    #part2 = music21.stream.Part(chords)

    sc = music21.stream.Score()
    sc.insert(0, melody_part)
    sc.insert(0, chord_part)

    midi_stream = music21.stream.Stream(sc)
    midi_stream.write('midi', fp='./a_new.mid')
    midi_stream.show()
    print('done')
    os.system('pause')
    # make 


if __name__ == '__main__':
    try:
        midi_files = glob.glob(argv[1])
        if len(midi_files) == 0:
            raise FileNotFoundError('Target file is not existed.')

        addTrack(midi_files[0])

    except IndexError as e:
        print(usage)
        
'''
    a = music21.converter.parse('./test_output.mid')
    print(a.track)
'''
