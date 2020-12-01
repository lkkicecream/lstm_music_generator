#判斷每小節是什麼調性

def whichkeys(Key):
    bigarr = []
    smallarr = []
    keyrule = []
    BorS = 0
    arr = str(Key)

    if (arr[0] == "C"):
        first = 60
        return first
    elif (arr[0] == "c"):
        BorS = 1
        first = 60
        return first
    elif (arr[0] == "D"):
        if (arr[1] == "-"):
            first = 61
            return first
        else:
            first = 62
            return first
    elif (arr[0] == "d"):
        BorS = 1
        if (arr[1] == "-"):
            first = 61
            return first
        else:
            first = 62
            return first
    elif (arr[0] == "E"):
        if (arr[1] == "-"):
            first = 63
            return first
        else:
            first = 64
            return first
    elif (arr[0] == "e"):
        BorS = 1
        if (arr[1] == "-"):
            first = 63
            return first
        else:
            first = 64
            return first
    elif (arr[0] == "F"):
        first = 65
        return first
    elif (arr[0] == "f"):
        BorS = 1
        first = 65
        return first
    elif (arr[0] == "G"):
        if (arr[1] == "-"):
            first = 66
            return first
        else:
            first = 67
            return first
    elif (arr[0] == "g"):
        BorS = 1
        if (arr[1] == "-"):
            first = 66
            return first
        else:
            first = 67
            return first
    elif (arr[0] == "A"):
        if (arr[1] == "-"):
            first = 68
            return first
        else:
            first = 69
            return first
    elif (arr[0] == "a"):
        BorS = 1
        if (arr[1] == "-"):
            first = 68
            return first
        else:
            first = 69
            return first
    elif (arr[0] == "B"):
        if (arr[1] == "-"):
            first = 70
            return first
        else:
            first = 71
            return first
    elif (arr[0] == "b"):
        BorS = 1
        if (arr[1] == "-"):
            first = 70
            return first
        else:
            first = 71
            return first






