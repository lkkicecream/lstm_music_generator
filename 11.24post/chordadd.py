import mido
import random
from mido import Message


def chordadd(chordbass, noterange):
    mid = mido.MidiFile("test.mid")
    trackbass = mido.MidiTrack()
    track1 = mido.MidiTrack()
    track2 = mido.MidiTrack()
    track3 = mido.MidiTrack()
    track4 = mido.MidiTrack()

    mid.tracks.append(trackbass)
    mid.tracks.append(track1)
    mid.tracks.append(track2)
    mid.tracks.append(track3)
    mid.tracks.append(track4)

    track4.append(Message('program_change', channel=1, program=10, time=0))
    trackbass.append(Message('program_change', channel=2, program=6, time=0))

    y = int(mid.ticks_per_beat)
    y = int(y/2)
    print(y)

    for data in chordbass:
        while (data < noterange[0]):
            data = data + 12
        while (data > noterange[6]):
            data = data - 12
        count = 0
        for rule in noterange:
            if(rule <= data):
                basic = count
            count = count + 1

        #高音鐵琴(3種節奏)
        num = random.randint(0, 3)

        if(num == 0):#2短1長

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y*2, channel=1))

        elif(num == 1):#1長2短

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y * 2, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y, channel=1))

        elif (num == 2):#4短

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=65, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=65, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=60, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=60, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=60, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=60, time=y, channel=1))

        elif (num == 3):#2長

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=60, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=60, time=y*2, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note]+12, velocity=70, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note]+12, velocity=70, time=y*2, channel=1))

        #低音Bass.
        num = random.randint(0, 1)

        if (num == 0):#2長
            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note] -24, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note] -24, velocity=70, time=y * 2, channel=1))

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note] -24, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note] -24, velocity=70, time=y * 2, channel=1))

        if (num == 1):  # 2短1長

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note] - 24, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note] - 24, velocity=70, time=y, channel=1))

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note] - 24, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note] - 24, velocity=70, time=y, channel=1))

            note = chordnote(basic)
            track4.append(mido.Message('note_on', note=noterange[note] - 24, velocity=70, time=0, channel=1))
            track4.append(mido.Message('note_off', note=noterange[note] - 24, velocity=70, time=y * 2, channel=1))

    mid.save("a1.mid")

def chordnote(basic):

    chordfirst = basic
    chordsecend = basic + 2
    chordthree = basic + 4
    num = random.randint(0, 2)
    if(num == 0):
        return chordfirst % 7
    elif(num == 1):
        return chordsecend % 7
    elif(num == 2):
        return chordthree % 7
