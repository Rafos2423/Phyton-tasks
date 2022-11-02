def get_words(path='words.txt'):
    f = open(path, 'r', encoding='utf-8')
    text = f.readlines()
    words = str(*text).split()
    f.close()
    return words

def write_record(record, file='record.txt'):
    f = open(file, 'r+', encoding='utf-8')
    old_record = f.read()
    if record < int(old_record):
        print('Новый рекорд!')
        f.seek(0)
        f.write(str(record))
    f.close()