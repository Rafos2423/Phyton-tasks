import math

n = int(input())
countSquares = int(math.sqrt(n))

for i in range(countSquares):
    print((i+1)**2)