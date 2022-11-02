string = input()
first = string.find("f")
second = string.rfind("f")

if first == second:
    print(first)
else:
    print(f'{first} {second}')