from chordadd import *
from whichkeys import *
import music21

def writemap(arr, arrtime, noterange):
    times = 0
    map = open("timamap.txt", "w")
    cut = 0
    timesnumber = []
    plzuse = []
    chordbass = []
    tones = []
    keys = [] #存每小節調性
    take_keyss = [] #這個小節調性的第一個音
    timesnumber.append(times)

    for data in arrtime:
        thisnote = int(data/2)
        if (thisnote != cut):
            map.write("\n")
            cut = thisnote
            timesnumber.append(times)
        map.write("\ ")
        map.write(str(data))
        times = times + 1

    timesnumber.append(times)
    x = 0
    notemap = open("notemap.txt", "w")

    while(x<=cut):
        op = timesnumber[x]
        ed = timesnumber[x+1]
        chordbass.append(arr[op])

        while(op<ed):
            notemap.write(str(arr[op]))
            notemap.write(" ")
            plzuse.append(int(arr[op]))
            op = op + 1
        #print(plzuse)

        for cor in plzuse:
            new_note = music21.note.Note(int(cor))  # 把当前音符化成整数，在对应midi_number转换成note
            new_note.storedInstrument = music21.instrument.Piano()  # 乐器用钢琴
            tones.append(new_note)
        midi_stream = music21.stream.Stream(tones)
        Key = music21.analysis.discrete.analyzeStream(midi_stream, 'key')
        keys.append(str(Key))

        plzuse = []
        tones = []
        notemap.write("\n")
        x = x + 1
    #print(chordbass)

    for data in keys:
            take_keyss.append(whichkeys(data))
    print(take_keyss)
    map.close()
    notemap.close()
    chordadd(noterange, take_keyss)

#chordbass 美小節第一個音(之後沒用到