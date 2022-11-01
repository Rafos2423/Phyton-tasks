import re

def read_file(name):
    f = open(name, 'r')
    text = f.read() #чтение из файла
    text = re.sub(r'[^\w\s]', '', text) #удаление пунктуации
    text = text.lower() #перевод в нижний регистр
    words = text.split() #разделение
    words = list(set(words)) #удаление повторов
    words.sort() #сортировка
    f.close()
    return words

def save_file(name, words):
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
