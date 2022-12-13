import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

tel_nums = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()
print(tel_nums)
namePattern = r'(?:__title-link\">)(\w+[^<]+)'
adressPattern = r'(?:meta--location\">\n\s+)([^\n]+)'
phonePattern = r'(?:Телефон</span></dt>\n+\s+<dd class=\"spec__value\">)([^<]+)'
timePattern = r'(?:Часы работы</span></dt>\n+\s+<dd class=\"spec__value\">)([^<]+)'

name = re.findall(namePattern, tel_nums)
adress = re.findall(adressPattern, tel_nums)
phone = re.findall(phonePattern, tel_nums)
time = re.findall(timePattern, tel_nums)

result = []

for i in range(len(name)-1):
    result.append([name[i], adress[i], phone[i], time[i]])
print(result)