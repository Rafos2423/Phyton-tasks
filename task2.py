book = {}
def input_command():
    print('Что вы хотите сделать?\n1 - Добавить\n2 - Удалить\n3 - Смотреть\n4 - Изменить\n5 - Выход')
    n = input()
    while not n.isdigit():
        print('Введите число:')
        n = input()
    return int(n)

def input_number():
    print('Введите телефон:')
    number = input()
    number = number.replace('-', '').replace(' ', '')
    return number.replace('8', '+7', 1) if number.isdigit and len(number) == 11 else 0

def input_name():
    print('Введите имя:')
    name = input()
    return name.title() if not name == '' else 0

while True:
    n = input_command()

    if n == 1:
        number = input_number()
        name = input_name()

        while name == 0:
            print('Имя не верно')
            number = input_number()
        while number == 0:
            print('Номер не верный')
            number = input_number()

        book[name] = number

    elif n == 2:
        name = input_name()

        while name == 0:
            print('Имя не верно')
            number = input_number()
        while not book.__contains__(name):
            print('Такого контакта нет')
            name = input_name()

        book.pop(name)
        print(f'Контакт {name} удален')
    elif n == 3:
        print(*book.items())

    elif n == 4:
        name = input_name()

        while name == 0:
            print('Имя не верно')
            number = input_number()
        while not book.__contains__(name):
            print('Такого контакта нет')
            name = input_name()

        number = input_number()
        while number == book[name]:
            print(f'Вы ввели тот же самый номер')
            number = input_number()

        book[name] = number
        print(f'Контакт {name} изменен')
    elif n == 5:
        break
