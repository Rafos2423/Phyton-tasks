import os
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image

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
              '2 - Преобразовать Doc, Docx в PDF\n'
              '3 - Сжать изображение\n'
              '4 - Удалить группу файлов\n'
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


def find_files(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            if format.__contains__(file.split('.')[-1]):
                files.append(file)

    for i in range(len(files)):
        print(f'{i + 1} - {files[i]}')

    return files

def choose_files(files, format):
    print('\nВыберите файл для конвертации (0-для всех файлов):')
    file_num = correct_input(0, len(files))

    if file_num == 0:
        for file in files:
            convert_file(file, format)
    else:
        convert_file(files[file_num - 1], format)

def convert_file(file, format):
    new_format_file = file.replace(file.split('.')[-1], format)
    try:
        parse(file, new_format_file)
    except:
        print(f'Невозможно преобразовать файл {file}')


#def compress_img(img):




catalog = os.getcwd()
print(f'Текущий каталог: {catalog}')

while True:
    option = menu()

    if option == 0:
        catalog = change_dir()
        print(f'Текущий каталог: {catalog}')

    if option == 1:
        pdf_files = find_files(catalog, ['pdf'])
        if len(pdf_files) == 0:
            print(f'В папке нет файлов формата pdf')
            continue

        choose_files(pdf_files, 'docx')

    if option == 2:
        docx_files = find_files(catalog, ['doc', 'docx'])
        if len(docx_files) == 0:
            print(f'В папке нет файлов формата doc, docx')
            continue

        choose_files(docx_files, 'pdf')

    if option == 3:
        image_file = find_files(catalog, ['jpeg', 'gif', 'png', 'jpg', 'img'])


    if option == 5:
        break
