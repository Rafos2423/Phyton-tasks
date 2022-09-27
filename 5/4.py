array = [1, 2, 3, 4, 5, 0]
count = 0
for i in range(len(array) - 1):
    if (array[i] < array[i + 1]):
        count += 1

print(count)
