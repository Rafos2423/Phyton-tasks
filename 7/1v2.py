str = input().split()
words = {}

for i in range(len(str)):
    if not str[i] in words:
        words[str[i]] = 0
    print(words[str[i]])
    words[str[i]] += 1