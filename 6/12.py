str = input()
first = str.find('h')
last = str.rfind('h')
print(f'{str[:first+1]}{str[first+1:last].replace("h", "H")}{str[last:]}')
