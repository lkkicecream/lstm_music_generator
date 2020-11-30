#判斷每小節是什麼調性

def whichkeys(Key):
    bigarr = []
    smallarr = []
    keyrule = []
    BorS = 0
    arr = str(Key)

    if (arr[0] is "C"):
        first = 60
        return first
    elif (arr[0] is "c"):
        BorS = 1
        first = 60
        return first
    elif (arr[0] is "D"):
        if (arr[1] is "-"):
            first = 61
            return first
        else:
            first = 62
            return first
    elif (arr[0] is "d"):
        BorS = 1
        if (arr[1] is "-"):
            first = 61
            return first
        else:
            first = 62
            return first
    elif (arr[0] is "E"):
        if (arr[1] is "-"):
            first = 63
            return first
        else:
            first = 64
            return first
    elif (arr[0] is "e"):
        BorS = 1
        if (arr[1] is "-"):
            first = 63
            return first
        else:
            first = 64
            return first
    elif (arr[0] is "F"):
        first = 65
        return first
    elif (arr[0] is "f"):
        BorS = 1
        first = 65
        return first
    elif (arr[0] is "G"):
        if (arr[1] is "-"):
            first = 66
            return first
        else:
            first = 67
            return first
    elif (arr[0] is "g"):
        BorS = 1
        if (arr[1] is "-"):
            first = 66
            return first
        else:
            first = 67
            return first
    elif (arr[0] is "A"):
        if (arr[1] is "-"):
            first = 68
            return first
        else:
            first = 69
            return first
    elif (arr[0] is "a"):
        BorS = 1
        if (arr[1] is "-"):
            first = 68
            return first
        else:
            first = 69
            return first
    elif (arr[0] is "B"):
        if (arr[1] is "-"):
            first = 70
            return first
        else:
            first = 71
            return first
    elif (arr[0] is "b"):
        BorS = 1
        if (arr[1] is "-"):
            first = 70
            return first
        else:
            first = 71
            return first






