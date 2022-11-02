n = int(input())

fib = []
fib.append(1)
fib.append(1)
length = 2

for i in range(2, n):
    fib.append(fib[length - 2] + fib[length - 1])
    length += 1

print(fib[length - 1])