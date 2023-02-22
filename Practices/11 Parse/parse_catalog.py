import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
input = urllib.request.urlopen("https://quke.ru/shop/smartfony/apple?page-size=72").read().decode()

price_pattern = r'(?:<span class="b-card2-v2__price-val">)([^<]+)'
price = re.findall(price_pattern, input)
print(price)

phone_pattern = r'(?:<a class="b-card2-v2__name" href=")(?:[^\"]+)(?:" title=")([^\"]+)'
phone = re.findall(phone_pattern, input)
print(phone)

phone_price = dict(map(lambda x, y: (x, int(y.replace(" ", ""))), phone, price))
phone_count = 72

lower_coast = min(phone_price.values())
higher_coast = max(phone_price.values())
average_coast = round(sum(phone_price.values()) / phone_count)

print(lower_coast)
print(higher_coast)
print(average_coast)

f = open("catalog.txt", 'w')
for k, v in phone_price.items():
    f.write(f'{k}: {v}\n')

f.write(f'\nmin: {str(lower_coast)} \n')
f.write(f'max: {str(higher_coast)} \n')
f.write(f'avg: {str(average_coast)} \n')