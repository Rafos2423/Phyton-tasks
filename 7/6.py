countCountries = int(input())
countries = {}

for i in range(countCountries):
    line = input().split()
    countries[line[0]] = list(line[1:])

countOperations = int(input())
result = []

for i in range(countOperations):
    city = input()

    contains = False
    for country in countries:
        if city in countries[country]:
            result.append(country)
            contains = True
            break

    if not contains:
        result.append('Not find country in base')

print(*result, sep='\n')
