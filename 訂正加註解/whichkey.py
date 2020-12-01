
#判斷整首曲子什麼調

def whichkey(Key):
    bigarr = []
    smallarr = []
    keyrule = []
    BorS = 0
    arr = str(Key)
    print(arr[0], arr[1])

    if (arr[0] == "C"):
        first = 60
    elif (arr[0] == "c"):
        BorS = 1
        first = 60
    elif (arr[0] == "D"):
        if (arr[1] == "-"):
            first = 61
        else:
            first = 62
    elif (arr[0] == "d"):
        BorS = 1
        if (arr[1] == "-"):
            first = 61
        else:
            first = 62
    elif (arr[0] == "E"):
        if (arr[1] == "-"):
            first = 63
        else:
            first = 64
    elif (arr[0] == "e"):
        BorS = 1
        if (arr[1] == "-"):
            first = 63
        else:
            first = 64
    elif (arr[0] == "F"):
        first = 65
    elif (arr[0] == "f"):
        BorS = 1
        first = 65
    elif (arr[0] == "G"):
        if (arr[1] == "-"):
            first = 66
        else:
            first = 67
    elif (arr[0] == "g"):
        BorS = 1
        if (arr[1] == "-"):
            first = 66
        else:
            first = 67
    elif (arr[0] == "A"):
        if (arr[1] == "-"):
            first = 68
        else:
            first = 69
    elif (arr[0] == "a"):
        BorS = 1
        if (arr[1] == "-"):
            first = 68
        else:
            first = 69
    elif (arr[0] == "B"):
        if (arr[1] == "-"):
            first = 70
        else:
            first = 71
    elif (arr[0] == "b"):
        BorS = 1
        if (arr[1] == "-"):
            first = 70
        else:
            first = 71

    if (BorS == 1):
        smallarr = [first, first+2, first+3, first+5, first+7, first+8, first+11]
        print(smallarr)
        return smallarr
    elif(BorS == 0):
        bigarr = [first, first+2, first+4, first+5, first+7, first+9, first+11]
        print(bigarr)
        return bigarr






