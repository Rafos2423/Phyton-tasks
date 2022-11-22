import re

def choose_complexity() -> int:
    '''
    Меню выбора сложности
    :return: количество попыток игрока
    '''
    choice = input('\nВыберите сложность: 1 - 3 жизни, 2 - 5 жизней, 3 - 7 жизней ')
    return (2 * int(choice) + 1) if choice == '1' or choice == '2' or choice == '3' else choose_complexity()

def check_input(word: str) -> str:
    '''
    Проверка ввода правильных символов
    :param word: загаданное слово
    :return: введенное слово
    '''
    n = input('\nВведите букву или слово: ')
    if re.findall(r'[а-яА-Я]', n) == []:
        check_input(word)
    return n

def play(word: str) -> int:
    '''
    Описание процесса игры. Проверка возможных вариантов победы и проигрыша
    :param word: загаданное слово
    :return: количество попыток - рекорд
    '''
    max_attemps = choose_complexity()
    attemps = max_attemps

    print_word = []
    for i in range(len(word)):
        print_word.append('\u25A0')
    print(*print_word)

    while attemps > 0:
        n = check_input(word)

        if len(n) == 1:
            if n in word:
                for i in range(len(word)):
                    if word[i] == n:
                        print_word[i] = n
                print('Вы угадали')
                print(*print_word)

                if not print_word.__contains__('\u25A0'):
                    print(f'Вы выиграли!')
                    return max_attemps - attemps
            else:
                attemps -= 1
                print(f'Вы не угадали. Ваши жизни {attemps}')
                print(*print_word)

        elif n == word:
            print(f'Вы выиграли!')
            return max_attemps - attemps
        else:
            attemps -= 1
            print(f'Вы не угадали. Ваши жизни {attemps}')
            print(*print_word)

    print(f'Вы проиграли! Слово было {word}')
    return max_attemps - attemps
