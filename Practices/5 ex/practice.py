text = []
try:
    file_name = input()
    f = open(file_name)
    count = int(f.readline())
    for i in range(count):
        text.append(f.readline())
    f.close()
    print('Очистка: Закрытие файла')
    print(text)
except KeyboardInterrupt:
    print('Вы отменили операцию')
except EOFError:
    print('Неверное количество строк')
except IOError:
    print('Невозможно прочитать файл')
except TypeError:
    print('Невозможно преобразовать строку в число')
except:
    print('Произошла непредвиденная ошибка')