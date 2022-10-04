import re

f = open('file.txt', 'r', encoding='utf-8')
text = f.readlines()

rasp = []
for line in text:
    info = re.match(r'(^Рейс\s\d{3}\s(?:прибыл|отправился)\s(?:из|в)\s\w{4,10}\sв\s\d{2}:\d{2}:\d{2})', line)

    if info != None:
        rasp.append(info[0])

f = open('newfile', 'a', encoding='utf-8')
f.write('\n'.join(rasp))