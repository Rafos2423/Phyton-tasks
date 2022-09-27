array = input().split()

count = 1
maxCount = 1
for i in range(len(array) - 1):
    if (array[i] == array[i+1]):
        count += 1
        if (count > maxCount):
            maxCount = count
    else:
        count = 1

print(maxCount)