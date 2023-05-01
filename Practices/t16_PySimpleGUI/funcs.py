import os
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image
import PySimpleGUI as sg


def correct_input(min_value, max_value):
    layout = [
        [sg.Text(f'Введите число от {min_value} до {max_value}:')],
        [sg.Input(key='-INPUT-')],
        [sg.Button('OK')]
    ]

    window = sg.Window('Ввод данных', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'OK':
            n = values['-INPUT-']
            if n.isdigit():
                if int(n) <= max_value and int(n) >= min_value:
                    window.close()
                    return int(n)
        sg.popup(f'Введите число от {min_value} до {max_value}')

    window.close()


def change_dir():
    layout = [
        [sg.Text('Укажите путь к каталогу:')],
        [sg.InputText(key='path')],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Сменить рабочий каталог', layout)

    while True:
        event, values = window.Read()

        if event is None or event == 'Cancel':
            window.Close()
            return None

        path = values['path']

        try:
            os.chdir(path)
            window.Close()
            return os.getcwd()
        except:
            sg.Popup('Неверный путь')


def convert_file(file):
    format_file = file.split('.')[-1]

    if format_file == 'pdf':
        new_file = file.replace(format_file, 'docx')

        try:
            parse(file, new_file)
        except:
            sg.Text(f'Невозможно преобразовать файл {file} в формат docx')

    elif format_file == 'doc' or format_file == 'docx':
        new_file = file.replace(format_file, 'pdf')

        try:
            convert(file, new_file)
        except:
            sg.Text(f'Невозможно преобразовать файл {file} в формат pdf')

    else:
        sg.Text('Укажите параметры сжатия в %:')
        quality = correct_input(1, 100)
        try:
            image_path = file
            image_file = Image.open(image_path)
            image_file.save(file, quality=quality)
        except:
            sg.Text(f'Невозможно сжать изображение')


def choose_files_gui(files):
    layout = [
        [sg.Text(f'Выберите файлы для изменения в папке "{files}"', font=('Helvetica', 14))],
        [sg.Listbox(values=files, size=(60, 20), key='FILES')],
        [sg.Submit('Выбрать', font=('Helvetica', 14)), sg.Cancel('Отмена', font=('Helvetica', 14))]
    ]
    window = sg.Window('Выбор файлов', layout)

    while True:
        event, values = window.read()

        if event == 'Выбрать':
            files = [os.path.join(files, file) for file in values['FILES']]
            window.close()
            return files

        if event in (sg.WINDOW_CLOSED, 'Отмена'):
            window.close()


def convert_file_gui(file):
    format_file = file.split('.')[-1]

    if format_file == 'pdf':
        new_file = file.replace(format_file, 'docx')

        try:
            parse(file, new_file)
            sg.Popup(f'Файл {file} успешно преобразован в формат docx')
        except:
            sg.Popup(f'Невозможно преобразовать файл {file} в формат docx')

    elif format_file == 'doc' or format_file == 'docx':
        new_file = file.replace(format_file, 'pdf')

        try:
            convert(file, new_file)
            sg.Popup(f'Файл {file} успешно преобразован в формат pdf')
        except:
            sg.Popup(f'Невозможно преобразовать файл {file} в формат pdf')

    else:
        layout = [
            [sg.Text('Укажите параметры сжатия в %:')],
            [sg.InputText(key='quality')],
            [sg.Submit()]
        ]

        window = sg.Window('Сжатие изображения', layout)

        while True:
            event, values = window.Read()

            if event is None:
                window.Close()
                return None

            quality = values['quality']

            if quality.isnumeric():
                quality = int(quality)
                break
            else:
                sg.Popup('Неверный ввод')

        try:
            image_path = file
            image_file = Image.open(image_path)
            image_file.save(file, quality=quality)
            sg.popup(f'Файл {file} успешно сжат')
        except:
            sg.popup_error(f'Невозможно сжать изображение {file}')


def find_files(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            if format.__contains__(file.split('.')[-1]):
                files.append(file)

    file_list = [f"{i+1} - {file}" for i, file in enumerate(files)]

    layout = [[sg.Listbox(file_list, size=(60, 10), key='FILES')], [sg.Button('OK'), sg.Button('Cancel')]]
    window = sg.Window('Files', layout)

    while True:
        event, values = window.Read()
        if event == 'OK':
            selected_files = [files[i] for i in values['FILES']]
            return selected_files
        elif event == 'Cancel' or event == None:
            break

    window.Close()


def change(dir, format):
    files = find_files(dir, format)
    if len(files) == 0:
        sg.popup(f'В папке нет файлов формата {", ".join(format)}')
        return

    choose_files_gui(files)

