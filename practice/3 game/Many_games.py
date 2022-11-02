import random

def choose_continue_game(words):
    if len(words) == 0:
        return False

    choice = input('Хотите сыграть еще? да/нет ')
    if choice == 'да':
        return True
    if choice == 'нет':
        return False
    choose_continue_game(words)

def find_word(words):
    word = random.choice(words)
    words.remove(word)
    return word
