n = int(input())

count = 0
firstNum = 1
secondNum = 0
buf = 0

while(True):
    count += 1
    buf = firstNum
    firstNum += secondNum
    secondNum = buf

    if (secondNum >= n):
        if (secondNum == n):
            print(count)
        else:
            print(-1)
        break