def get_words(path = 'words.txt'):
    f = open(path, 'r', encoding='utf-8')
    text = f.readlines()
    return text