n = int(input())

fib = []
fib.append(1)
fib.append(1)
length = 2

while(True):
    fib.append(fib[length - 2] + fib[length - 1])
    length += 1

    if (n <= fib[length - 1]):
        if (n == fib[length - 1]):
            print(length)
        else:
            print(-1)
        break