n = int(input())
words = {}

for i in range(n):
    line = input().split()
    words[line[0]] = line[1]

requireValue = input()

for i in words:
    if words[i] == requireValue:
        print(i)
        break