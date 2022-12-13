book = {}
def menu():
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
    number = number.replace('+7', '8', 1)
    return number.replace('8', '+7', 1) if number.isdigit and len(number) == 11 else input_number()

def input_name():
    print('Введите имя:')
    name = input()
    name = name.split()
    name = ' '.join(name)
    return name.title() if not name == '' else input_name()

def add():
    number = input_number()
    name = input_name()

    book[name] = number

def remove():
    name = input_name()

    while not book.__contains__(name):
        print('Такого контакта нет')
        name = input_name()

    book.pop(name)
    print(f'Контакт {name} удален')

def print_dict():
    print(*book.items())

def change():
    name = input_name()

    while not book.__contains__(name):
        print('Такого контакта нет')
        name = input_name()

    number = input_number()
    while number == book[name]:
        print(f'Вы ввели тот же самый номер')
        number = input_number()

    book[name] = number
    print(f'Контакт {name} изменен')

while True:
    n = menu()

    if n == 1:
        add()

    elif n == 2:
        remove()

    elif n == 3:
        print_dict()

    elif n == 4:
        change()

    elif n == 5:
        break
