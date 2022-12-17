import os
from pdf2docx import parse
from docx2pdf import convert

def correct_input(min_value, max_value):
    n = input()
    if n.isdigit():
        if int(n) <= max_value and int(n) >= min_value:
            return int(n)

    print(f'\nВведите число от {min_value} до {max_value}')
    return correct_input(min_value, max_value)

def menu():
    print('\nВыберите действие\n'
              '0 - Сменить рабочий каталог\n'
              '1 - Преобразовать PDF в Docx\n'
              '2 - Преобразовать Docx в PDF\n'
              '3 - Сжать изображение\n'
              '4 - Сжать изображение\n'
              '5 - Выход')

    return correct_input(0, 5)


def change_dir():
    path = input('Укажите путь к каталогу: ')

    try:
        os.chdir(path)
    except:
        print('\nНеверный путь')
        change_dir()

    return os.getcwd()


def choose_file(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            if file.split('.')[-1] == format:
                files.append(file)

    if len(files) == 0:
        print(f'В папке нет файлов формата {format}')
        return None

    for i in range(len(files)):
        print(f'{i+1} - {files[i]}')

    print('\nВыберите файл для конвертации:')
    file_num = correct_input(1, len(files))
    return files[file_num - 1]


catalog = os.getcwd()
print(f'Текущий каталог: {catalog}')

while True:
    option = menu()

    if option == 0:
        catalog = change_dir()
        print(f'Текущий каталог: {catalog}')

    if option == 1:
        pdf_file = choose_file(catalog, 'pdf')
        if pdf_file == None:
            continue
        docx_file = pdf_file.replace('pdf', 'docx')
        parse(pdf_file, docx_file)

    if option == 2:
        docx_file = choose_file(catalog, 'docx')
        if docx_file == None:
            continue
        convert(docx_file)


    if option == 5:
        break
