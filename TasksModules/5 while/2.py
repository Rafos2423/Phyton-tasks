n = int(input())
pow = 0

while(True):
    n /= 2
    if (n < 1):
        break
    pow += 1

print(f'{pow} {2**pow}')