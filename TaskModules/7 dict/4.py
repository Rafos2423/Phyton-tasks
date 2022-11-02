n = int(input())
words = {}

for i in range(n):
    line = input().split()

    for j in range(len(line)):
        if not line[j] in words:
            words[line[j]] = 0
        words[line[j]] += 1

maxvalue = 1
oftenWords = {}

for i in words:
    if words[i] > maxvalue:
        maxvalue = words[i]

for i in words:
    if words[i] == maxvalue:
        oftenWords[i] = words[i]

oftenWords = dict(sorted(oftenWords.items()))

for i in oftenWords:
    print(i)
    break