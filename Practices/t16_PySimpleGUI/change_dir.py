import os
import PySimpleGUI as sg


def change_dir():
    layout = [
        [sg.Text('Текущая директория:'), sg.Text(os.getcwd(), key='dir')],
        [sg.Text('Выберите новую директорию:'), sg.FolderBrowse('Найти')],
        [sg.Button('Перейти'), sg.Button('Выход')]
    ]
    window = sg.Window('Смена директории', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Выход':
            break
        elif event == 'Перейти':
            if values['Найти'] == '':
                sg.popup('Директория не изменена')
            else:
                new_dir = values['Найти']
                os.chdir(new_dir)
                sg.popup(f'Текущая директория изменена на {new_dir}')
                break

    window.close()
    return os.getcwd()