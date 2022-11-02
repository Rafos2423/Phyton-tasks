str = input().split()
words = dict.fromkeys(str, 0)

for i in range(len(str)):
    print(words[str[i]])
    words[str[i]] += 1