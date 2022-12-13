import random

def choose_continue_game(words: list[str]) -> bool:
    '''

    :param words: список слов для игры
    :return: выбор пользователя продолжения игры
    '''
    if len(words) == 0:
        return False

    choice = input('Хотите сыграть еще? да/нет ')
    if choice == 'да':
        return True
    if choice == 'нет':
        return False
    choose_continue_game(words)

def find_word(words: list[str]) -> str:
    '''

    :param words: список слов для игры
    :return: случайное слово из списка
    '''
    print(words)
    word = random.choice(words)
    words.remove(word)
    return word
