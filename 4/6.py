n = int(input())

if (n / 100 <= (n / 10) % 10 and (n / 10) % 10 <= n % 10):
    print('Да')
else:
    print('Нет')