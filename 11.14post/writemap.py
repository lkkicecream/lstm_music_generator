
def writemap(arr, arrtime):
    times = 0
    map = open("timamap.txt", "w")
    #time = open("time.txt", "w")
    cut = 0
    timesnumber = []
    plzuse = []
    #time.write(str(times))
    #time.write("\ ")
    timesnumber.append(times)

    for data in arrtime:
        thisnote = int(data/2)
        if (thisnote != cut):
            map.write("\n")
            cut = thisnote
            #time.write(str(times))
            #time.write("\ ")
            timesnumber.append(times)
        map.write("\ ")
        map.write(str(data))
        times = times + 1

    #time.write(str(times))
    #time.write("\ ")
    timesnumber.append(times)
    x = 0
    notemap = open("notemap.txt", "w")

    while(x<=cut):
        op = timesnumber[x]
        ed = timesnumber[x+1]

        while(op<ed):
            notemap.write(str(arr[op]))
            notemap.write(" ")
            plzuse.append(int(arr[op]))
            op = op + 1
        print(plzuse)
        plzuse = []
        notemap.write("\n")
        x = x + 1

    #print(cut)
    #print(timesnumber[cut])
    map.close()
    #time.close()
    notemap.close()
