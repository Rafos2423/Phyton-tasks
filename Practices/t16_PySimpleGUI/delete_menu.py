import os
import PySimpleGUI as sg


def menu_delete():
    layout = [[sg.Text('Выберите действие:')],
              [sg.Radio('Удалить все файлы начинающиеся с подстроки', 'delete_group_files_menu', key='option_1'),
               sg.Radio('Удалить все файлы заканчивающиеся на подстроку', 'delete_group_files_menu', key='option_2'),
               sg.Radio('Удалить все файлы содержащие подстроку', 'delete_group_files_menu', key='option_3'),
               sg.Radio('Удалить все файлы по расширению', 'delete_group_files_menu', key='option_4')],
              [sg.Text('Введите подстроку:'), sg.Input(key='sub_string')],
              [sg.Button('Удалить'), sg.Button('Отмена')]]

    window = sg.Window('Delete Group of Files', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Отмена':
            window.close()
            return None

        if not values['sub_string']:
            sg.popup('Введите подстроку!')
            continue

        if not any(values.values()):
            sg.popup('Выберите действие!')
            continue

        if values['option_1']:
            delete_option = 1
        elif values['option_2']:
            delete_option = 2
        elif values['option_3']:
            delete_option = 3
        else:
            delete_option = 4

        window.close()
        return delete_option, values['sub_string']


def delete_group_files(catalog):
    delete_option, sub_string = menu_delete()

    if delete_option is None:
        return

    files = [file for file in os.listdir(catalog) if os.path.isfile(os.path.join(catalog, file))]
    delete_files = []

    if delete_option == 1:
        for file in files:
            if file.startswith(sub_string):
                delete_files.append(os.path.join(catalog, file))

    elif delete_option == 2:
        for file in files:
            filename = os.path.splitext(file)[0]
            if filename.endswith(sub_string):
                delete_files.append(os.path.join(catalog, file))

    elif delete_option == 3:
        for file in files:
            filename = os.path.splitext(file)[0]
            if sub_string in filename:
                delete_files.append(os.path.join(catalog, file))

    elif delete_option == 4:
        for file in files:
            if file.endswith('.' + sub_string):
                delete_files.append(os.path.join(catalog, file))

    if not delete_files:
        sg.popup('Нет файлов для удаления!')
        return

    layout = [[sg.Text('Вы действительно хотите удалить файлы?')],
              [sg.Listbox(values=delete_files, size=(70, 10))],
              [sg.Button('Да'), sg.Button('Нет')]]

    window = sg.Window('Delete Group of Files', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Нет':
            window.close()
            return

        if event == 'Да':
            for file in delete_files:
                os.remove(file)
            sg.popup('Файлы успешно удалены!')
            window.close()
            return
