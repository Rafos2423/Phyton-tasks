str = input()
first = str.find('h')
last = str.rfind('h')
print(f'{str[:first]}{str[last:first:-1]}{str[last:]}')