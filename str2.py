string = input()
indexSpace = string.find(" ")
print(f'{string[indexSpace+1:]} {string[:indexSpace]}')