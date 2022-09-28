n = int(input())
words = {}

for i in range(n):
    line = input().split()
    words[line[0]] = line[1]

requireValue = input()

for key, value in words.items():
    if value == requireValue:
        print(key)
        break