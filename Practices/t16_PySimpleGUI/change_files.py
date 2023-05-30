import os
import PySimpleGUI as sg
from docx2pdf import convert
from pdf2docx import parse
from PIL import Image

def find_files(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            if format.__contains__(file.split('.')[-1]):
                files.append(file)

    return files


def convert_file(file):
    format_file = file.split('.')[-1]

    if format_file == 'pdf':
        new_file = file.replace(format_file, 'docx')

        try:
            parse(file, new_file)
        except:
            sg.popup(f'Невозможно преобразовать файл {file} в формат docx')

    elif format_file == 'doc' or format_file == 'docx':
        new_file = file.replace(format_file, 'pdf')

        try:
            convert(file, new_file)
        except:
            sg.popup(f'Невозможно преобразовать файл {file} в формат pdf')

    else:
        layout = [[sg.Text('Укажите параметры сжатия в %:'),
                   sg.Input(key='quality', size=(5, 1)), sg.Button('Сжать'),
                   sg.Button('Отмена')]]

        window = sg.Window('Сжатие изображений', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Отмена':
                break

            if event == 'Сжать':
                quality = values['quality']

                try:
                    image_path = file
                    image_file = Image.open(image_path)
                    image_file.save(file, quality=quality)
                    break
                except:
                    sg.popup(f'Невозможно сжать изображение {file}')

        window.close()


def change(dir, format):
    files = find_files(dir, format)
    if len(files) == 0:
        sg.popup(f'В папке нет файлов формата {", ".join(format)}')
        return

    layout = [[sg.Text('Выберите файлы для конвертации:')],
              [sg.Listbox(values=files, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(40, 10), key='files')],
              [sg.Button('Конвертировать'), sg.Button('Отмена')]]

    window = sg.Window('Конвертер файлов', layout)

    while True:
        event, values = window.read()

        if event in (None, 'Отмена'):
            break

        if event == 'Конвертировать':
            selected_files = values['files']
            for file in selected_files:
                convert_file(os.path.join(dir, file))

            sg.popup('Конвертация завершена')
            break

    window.close()

