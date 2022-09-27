n = int(input())

if (n == 2):
    print('number is simple')

for i in range(2, n):
    if (i == n - 1): #n=2 не подходит под этот случай
        print('number is simple')
    if (n % i == 0):
        print(i)
        break
