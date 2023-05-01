import PySimpleGUI as sg

from Practices.t16_PySimpleGUI.delete_menu import delete_group_files
from Practices.t16_PySimpleGUI.funcs import *

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
print(f'Текущий каталог: {catalog}')

while True:
    event, values = window.Read()
    if event is None or event == 'exit':
        break
    if event == 'execute':
        if values['change_dir']:
            catalog = change_dir()
            print(f'Текущий каталог: {catalog}')
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
            delete_group_files(catalog)
            pass

window.Close()
