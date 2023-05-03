import os
import PySimpleGUI as sg


def menu_delete():
    layout = [
        [sg.Text('Выберите тип удаления')],
        [sg.Radio('Удалить файлы, начинающиеся с подстроки', "RADIO1", default=True, key='option1')],
        [sg.Radio('Удалить файлы, оканчивающиеся подстрокой', "RADIO1", key='option2')],
        [sg.Radio('Удалить файлы, содержащие подстроку в названии', "RADIO1", key='option3')],
        [sg.Radio('Удалить файлы с расширением подстроки', "RADIO1", key='option4')],
        [sg.Button('Удалить'), sg.Button('Отмена')]
    ]

    window = sg.Window('Удаление файлов', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Отмена':
            window.close()
            return None

        if event == 'Удалить':
            if values['option1']:
                window.close()
                return 1
            elif values['option2']:
                window.close()
                return 2
            elif values['option3']:
                window.close()
                return 3
            elif values['option4']:
                window.close()
                return 4


def delete(catalog):
    delete_option = menu_delete()

    if delete_option is None:
        return

    sub_string = sg.popup_get_text('Введите подстроку:')

    files = []
    for file in os.listdir(catalog):
        if os.path.isfile(file):
            files.append(file)

    delete_files = []

    if delete_option == 1:
        for file in files:
            if file[0:len(sub_string)] == sub_string:
                delete_files.append(file)

    if delete_option == 2:
        for file in files:
            filename = file.split('.')[0]
            if filename[-len(sub_string):] == sub_string:
                delete_files.append(file)

    if delete_option == 3:
        for file in files:
            filename = file.split('.')[0]
            if filename.__contains__(sub_string):
                delete_files.append(file)

    if delete_option == 4:
        for file in files:
            format = file.split('.')[1]
            if format == sub_string:
                delete_files.append(file)

    if len(delete_files) == 0:
        sg.popup('Файлы для удаления не найдены')
        return

    layout = [
        [sg.Text('Вы действительно хотите удалить файлы?')],
        [sg.Listbox(delete_files, size=(50, len(delete_files)))],
        [sg.Button('Да'), sg.Button('Нет')]
    ]

    window = sg.Window('Удаление файлов', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Нет':
            window.close()
            break

        if event == 'Да':
            for file in delete_files:
                os.remove(file)
            sg.popup('Файлы успешно удалены')
            window.close()
            break