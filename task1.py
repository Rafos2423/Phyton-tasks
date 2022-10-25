import random

attemps = 3
record = 0

while True:
    if attemps == 0:
        print(f'Your record {record}, game over')
        break

    a = random.randint(10, 20)
    b = random.randint(0, 10)
    operation = random.randint(0, 1)
    if operation == 0:
        print(f'{a} + {b} = ?')
    else:
        print(f'{a} - {b} = ?')

    result = input()
    if (result.isdigit()):
        if ((operation == 0) and ((a + b) == int(result))):
            record += 1
            print(f'win, your record {record}')
        elif((operation == 1) and ((a - b) == int(result))):
            record += 1
            print(f'win, your record {record}')
        else:
            attemps -= 1
            print(f'false, your attemps {attemps}')
    else:
        print('not number')

