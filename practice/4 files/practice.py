import re

def read_file(name: str) -> list[str]:
    '''

    :param name: путь к файлу чтения
    :return: список отсортированных уникальных слов без спец симоволов
    '''
    f = open(name, 'r')
    text = f.read() #чтение из файла
    text = re.sub(r'[^\w\s]', '', text) #удаление пунктуации
    text = text.lower() #перевод в нижний регистр
    words = text.split() #разделение
    words = list(set(words)) #удаление повторов
    words.sort() #сортировка
    f.close()
    return words

def save_file(name: str, words: list[str]) -> None:
    '''

    :param name: путь к файлу записи
    :param words: список слов
    :return:
    '''
    f = open(name, 'r')
    text = f.read()
    if len(text) != 0:
        f.seek(0)
        f.close()
        return 0

    f = open(name, 'a')
    f.write(f'Всего уникальных слов: {str(len(words))} \n================\n')
    f.write('\n'.join(words))
    f.close()

words = read_file('data.txt')
save_file("count.txt", words)
