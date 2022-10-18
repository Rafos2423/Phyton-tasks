import re

f = open('file.txt', 'r', encoding='utf-8')
text = f.readlines()

data = []
for line in text:
    info = re.match(r'(^Рейс\s\d{3}\s(?:прибыл|отправился)\s(?:из|в)\s\w{4,10}\sв\s\d{2}:\d{2}:\d{2})', line)

    if info != None:
        data.append(info[0])

rasp = []
for i in range(len(data)):
    time = re.search(r'\d{2}:\d{2}:\d{2}', data[i])
    train_number = re.search(r'\d{3}', data[i])
    town = re.search(r'\w{4,10}', data[i])
    where = re.search(r'(?:из|в)', data[i])
    line = f'[{time}] - Поезд № {train_number} {where} {town} \n}'
    rasp.append(line)

f = open('newfile', 'a', encoding='utf-8')
f.write('\n'.join(data))