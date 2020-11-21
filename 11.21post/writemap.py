from chordadd import *

def writemap(arr, arrtime):
    times = 0
    map = open("timamap.txt", "w")
    cut = 0
    timesnumber = []
    plzuse = []
    chordbass = []
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
        plzuse = []
        notemap.write("\n")
        x = x + 1
    #print(chordbass)
    map.close()
    notemap.close()
    chordadd(chordbass)
