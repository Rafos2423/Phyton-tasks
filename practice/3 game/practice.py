import random

def get_words(path = 'words.txt'):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    return text.split()

def right_move():
    print(*print_word)

def false_move(attemps):
    print(f'False, your attemps: {attemps}')

def win():
    print(f'You win! The word is: {word}')

def lose():
    print(f'You lose! The word is: {word}')


def next_game():
    print('Do you want to play again? Press yes')
    choice = input()
    return True if choice == 'yes' else False


def complexity_game():
    print('Choose complexity: 1 - 3 lives, 2 - 5 lives, 3 - 7 lives')
    choice = input()
    return (2 * int(choice) + 1) if choice == '1' or choice == '2' or choice == '3' else  complexity_game()


def player_lose(a):
    a -= 1
    if a == 0:
        lose()
    else:
        false_move(attemps)
    return a

def Check(letter, word):
    if letter in word:
        if "_" in print_word:
            win()
        else:
            right_move()
        return True
    else:
        return False

def


while True:
    words = get_words()
    word = random.choice(words)
    words.remove(word)

    attemps = complexity_game()

    print_word = []
    for i in range(len(word)):
        print_word.append('\u25A0')

    while attemps > 0:
        print('Name the letter or word: ')
        n = input()

        if len(n) == 1: #игрок угадывает букву из слова
            if n in word:
                if not print_word.__contains__("_"):
                    win()
                    break
                else:
                    right_move()
            else:
                attemps = player_lose(attemps)

        elif len(n) == len(word): #игрок угадывает слово
            if n == word:
                win()
                break
            else:
                attemps = player_lose(attemps)

        else:
            print('Enter a letter or a word')

    if len(words) == 0 or not next_game():
        print('The game end. Good luck!')
        break