import PySimpleGUI as sg
import os

from Practices.t16_PySimpleGUI.change_dir import change_dir
from Practices.t16_PySimpleGUI.change_files import change
from Practices.t16_PySimpleGUI.delete_files import delete

layout = [
    [sg.Text('Выберите действие:')],
    [sg.Radio('Сменить рабочий каталог', "action", default=True, key='change_dir')],
    [sg.Radio('Преобразовать PDF в Docx', "action", key='pdf_to_docx')],
    [sg.Radio('Преобразовать Doc, Docx в PDF', "action", key='doc_to_pdf')],
    [sg.Radio('Сжать изображение', "action", key='compress_image')],
    [sg.Radio('Удалить группу файлов', "action", key='delete_files')],
    [sg.Button('Выполнить', key='execute'), sg.Button('Выход', key='exit')]
]

window = sg.Window('Менеджер файлов').Layout(layout)

catalog = os.getcwd()

while True:
    event, values = window.Read()
    if event is None or event == 'exit':
        break
    if event == 'execute':
        if values['change_dir']:
            catalog = change_dir()
            pass

        elif values['pdf_to_docx']:
            change(catalog, ['pdf'])
            pass

        elif values['doc_to_pdf']:
            change(catalog, ['doc', 'docx'])
            pass

        elif values['compress_image']:
            change(catalog, ['img', 'png', 'jpg', 'jpeg', 'bmp'])
            pass

        elif values['delete_files']:
            delete(catalog)
            pass

window.Close()
