import mido
import random
from mido import Message

#加上其他聲部
def chordadd(noterange, takekeyss):
    mid = mido.MidiFile("test.mid")
    #先宣告track
    trackbass = mido.MidiTrack()
    track4 = mido.MidiTrack()

    mid.tracks.append(trackbass)
    mid.tracks.append(track4)

    #這幾個事測試用的
    track1 = mido.MidiTrack()
    track2 = mido.MidiTrack()
    track3 = mido.MidiTrack()

    mid.tracks.append(track1)
    mid.tracks.append(track2)
    mid.tracks.append(track3)

    #這裡是變換樂器，但不好聽所以先註解掉
    #trackbass.append(Message('program_change', channel=2, program=3, time=0))
    #track4.append(Message('program_change', channel=1, program=8, time=0))

    #y是測出這首曲子的拍子的數值是多少
    y = int(mid.ticks_per_beat)
    y = int(y)
    print(y)


    for data in takekeyss:

        #把takekeyss裡的資料調整到同一個八度
        while (data < noterange[0]):
            data = data + 12
        while (data > noterange[6]):
            data = data - 12

        #確認資料是什麼音
        count = 0
        for rule in noterange:
            if (rule <= data):
                basic = count
            count = count + 1

        '''
        #測試用
        test = chordnotetest(basic)

        track1.append(mido.Message('note_on', note=noterange[test[0]], velocity=65, time=0, channel=1))
        track1.append(mido.Message('note_off', note=noterange[test[0]], velocity=65, time=y * 4, channel=1))

        track2.append(mido.Message('note_on', note=noterange[test[1]], velocity=65, time=0, channel=1))
        track2.append(mido.Message('note_off', note=noterange[test[1]], velocity=65, time=y * 4, channel=1))

        track3.append(mido.Message('note_on', note=noterange[test[2]], velocity=65, time=0, channel=1))
        track3.append(mido.Message('note_off', note=noterange[test[2]], velocity=65, time=y * 4, channel=1))
        '''

        #高音鐵琴(3種節奏)
        num = random.randint(0, 3)

        if(num == 0):#2短1長

            note = chordnote(basic) #讓基礎音隨機生成其大三和弦中的任一音
            #將生成的音加入音樂中
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
            trackbass.append(mido.Message('note_on', note=noterange[note]-12, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note]-12, velocity=70, time=y * 2, channel=1))

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note]-12, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note]-12, velocity=70, time=y * 2, channel=1))

        if (num == 1):  # 2短1長

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note]-12, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note]-12, velocity=70, time=y, channel=1))

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note]-12, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note]-12, velocity=70, time=y, channel=1))

            note = chordnote(basic)
            trackbass.append(mido.Message('note_on', note=noterange[note]-12, velocity=70, time=0, channel=1))
            trackbass.append(mido.Message('note_off', note=noterange[note]-12, velocity=70, time=y * 2, channel=1))

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

'''
def chordnotetest(basic):

    test = []
    chordfirst = basic
    chordsecend = basic + 2
    chordthree = basic + 4

    test.append(chordfirst % 7)
    test.append(chordsecend % 7)
    test.append(chordthree % 7)

    return test
'''