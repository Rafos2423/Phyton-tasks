import random

agree = 0
not_agree = 0

for i in range(100000):
    a = [0, 0, 1]

    choice = random.randint(0, 2)
    a.pop(choice)
    a.remove(0)

    if a[0] == 1:
        agree += 1
    else:
        not_agree += 1

print(f'agree: {agree/1000}\nnot agree: {not_agree/1000}')



