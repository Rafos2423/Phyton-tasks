import re

f = open('file.txt', 'r', encoding='utf-8')
text = f.readlines()

data = []
for line in text:
    info = re.match(r'(^Рейс\s\d{3}\s(?:прибыл|отправился)\s(?:из|в)\s\w{4,10}\sв\s\d{2}:\d{2}:\d{2})', line)

    if info != None:
        data.append(info[0])

rasp = []
for line in data:
    time = re.search(r'\d{2}:\d{2}:\d{2}', line).group(0)
    train_number = re.search(r'\d{3}', line).group(0)
    town = re.search(r'(?:из|в)\s\w{4,10}', line).group(0)
    rasp.append(f'[{time}] - Поезд № {train_number} {town}')

f = open('newfile', 'a', encoding='utf-8')
if len(text) != 0:
    f.seek(0)

f.write('\n'.join(rasp))
