import random

def game(iterations: int) -> str:
    '''

    :param iterations: кол-во повторов
    :return: процент побед если игрок согласится с ведущим и процент если нет
    '''
    agree = 0
    not_agree = 0

    for i in range(iterations):
        a = [0, 0, 1]

        choice = random.randint(0, 2) #выбор игрока
        a.pop(choice) #карта игрока открывается
        a.remove(0) #ведущий открывает карту

        if a[0] == 1: #если последняя карта верная, то игрок походил бы правильно если бы поменял свое решение
            agree += 1
        else: #иначе ему надо было оставить свою карту
            not_agree += 1

    return f'agree: {agree/iterations * 100}\nnot agree: {not_agree/iterations * 100}'




