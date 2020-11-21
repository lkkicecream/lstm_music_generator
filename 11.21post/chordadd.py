import mido
from mido import Message


def chordadd(chordbass):
    mid = mido.MidiFile("test.mid")
    trackmain = mido.MidiTrack()
    track1 = mido.MidiTrack()
    track2 = mido.MidiTrack()
    track3 = mido.MidiTrack()
    track4 = mido.MidiTrack()

    mid.tracks.append(trackmain)
    mid.tracks.append(track1)
    mid.tracks.append(track2)
    mid.tracks.append(track3)
    mid.tracks.append(track4)

    #track4.append(Message('program_change', channel=0, program=8, time=0))


    y = int(mid.ticks_per_beat)
    y = int(y)
    print(y)

    for data in chordbass:
        data = data - 24
        '''        
        track1.append(mido.Message('note_on', note=data, velocity=70, time=0))
        track1.append(mido.Message('note_off', note=data, velocity=70, time=y))

        track2.append(mido.Message('note_on', note=data+4, velocity=70, time=0))
        track2.append(mido.Message('note_off', note=data+4, velocity=70, time=y))

        track3.append(mido.Message('note_on', note=data+7, velocity=70, time=0))
        track3.append(mido.Message('note_off', note=data+7, velocity=70, time=y))
        '''

        track4.append(mido.Message('note_on', note=data, velocity=70, time=0))
        track4.append(mido.Message('note_off', note=data, velocity=70, time=y))

        track4.append(mido.Message('note_on', note=data + 4, velocity=70, time=0))
        track4.append(mido.Message('note_off', note=data + 4, velocity=70, time=y))
        '''
        track4.append(mido.Message('note_on', note=data + 7, velocity=70, time=0))
        track4.append(mido.Message('note_off', note=data + 7, velocity=70, time=y))

        track4.append(mido.Message('note_on', note=data + 12, velocity=70, time=0))
        track4.append(mido.Message('note_off', note=data + 12, velocity=70, time=y))
        '''

    mid.save("a1.mid")


