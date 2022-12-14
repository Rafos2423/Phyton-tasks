lines = int(input())
wordsCount = {}

for i in range(lines):
    line = input().split()

    for i in range(len(line)):
        if not line[i] in wordsCount:
            wordsCount[line[i]] = 0
        wordsCount[line[i]] += 1

result = []

for key, value in wordsCount.items():
    result.append(f'{value} {key}')

result.sort()
result.reverse()

for i in range(len(result)):
    line = result[i].split()
    print(f'{line[1]} {line[0]}')