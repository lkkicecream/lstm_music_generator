import json
import random
import math

rhythm = []
with open('./musicTheory/rythem.json','r') as _:
    rythem = json.loads(_.read())

def combineRhythm(beats:int=1):
    combList = []
    while beats > 0:
        randList1 = random.choice(rythem)
        if len(randList1)==0:
            continue
        randList2 = random.choice(randList1)
        combList = combList + randList2
        beats -= rythem.index(randList1)
    return combList
# print(combineRythem(4))

#print(type(rythem[1][0][0]))