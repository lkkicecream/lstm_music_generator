import fire
import mido
from pretty_midi import *
from addmusic import *
from writemap import *
from getstart import *
from whichkey import *
import os
import numpy as np
#from music import *
from pathlib import Path
from printnote import *
from addmusic import *


""" The lstm generator CLI

you can use our command to optimize your midi file.

"""

if __name__ == '__main__':
  fire.Fire({
    'beancase': beancase,
    'split': get_note_Done,
    'getstart': getstart,
    'restart':restart,
    'chordadd':chordadd,
    'chordnote':chordnote,
    'whichkey':whichkey,
    'whichkeys':whichkeys,
    'writemap':writemap,
    'add':add,
    'bass':bass,
  })