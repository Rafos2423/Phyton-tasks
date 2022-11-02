x = int(input())
y = int(input())

if (y < x):
    print('sportsman is very strong!')

else:
    days = 1
    while(x <= y):
        x *= 1.1
        days += 1

    print(days)