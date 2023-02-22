import re
import ssl
import urllib.request
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context
input = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f").read().decode()
print(input)

now = datetime.now()
time = now.strftime("%H:%M:%S")

town = re.findall(r'(?:name\":")([^"]+)', input)
temp = re.findall(r'(?:temp\":)([^,]+)', input)
desc = re.findall(r'(?:description\":")([^"]+)', input)
hum = re.findall(r'(?:humidity\":)([^,]+)', input)
speed = re.findall(r'(?:speed\":)([^,]+)', input)
pressure = re.findall(r'(?:pressure\":)([^,]+)', input)

print(f'[{time}] Запрос погоды в городе: {town[0]}')
print(f'Температура: {temp[0]} C, {desc[0]}')
print(f'Влажность воздуха: {hum[0]}%')
print(f'Скорость воздуха: {speed[0]}м/с')
print(f'Атмосферное давление: {pressure[0]}мм рт. ст.')