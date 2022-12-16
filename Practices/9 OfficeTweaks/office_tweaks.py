import os

def menu():
    n = input('Выберите действие\n'
          '0 - Сменить рабочий каталог\n'
          '1 - Преобразовать PDF в Docx\n'
          '2 - Преобразовать Docx в PDF\n'
          '3 - Сжать изображение\n'
          '4 - Сжать изображение\n'
          '5 - Выход')

    if n.isdigit():
        if int(n) <= 5 and int(n) >= 0:
            return int(n)

    print('\nВведите число от 0 до 5')
    return menu()

def change_dir():
    path = input('Укажите путь к каталогу: ')

    try:
        os.chdir(path)
    except:
        print('\nНеверный путь')
        change_dir()

    return path

while True:
    catalog = os.getcwd()
    print(f'Текущий каталог: {catalog}\n')

    option = menu()

    if option == 0:
        catalog = change_dir()
        print(f'Текущий каталог: {catalog}\n')

    if option == 5:
        break
