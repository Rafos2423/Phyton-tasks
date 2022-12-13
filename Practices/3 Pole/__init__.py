import sys
import os

sys.path.append(os.path.dirname(__file__))

from .Game import *
from .File import *
from .Many_games import *


words = get_words()

while True:
    word = find_word(words)
    record = play(word)
    write_record(record)
    if not choose_continue_game(words):
        break