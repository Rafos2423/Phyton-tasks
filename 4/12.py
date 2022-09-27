def CalculateDaysInMonth(month):
    daysInMonth = 0

    if (month == 2):
        daysInMonth = 28
    else:
        if (month > 8):
            month -= 1
        if (month % 2 == 1):
            daysInMonth = 31
        else:
            daysInMonth = 30

    return daysInMonth

year = 2022
month = int(input())
day = int(input())

if (day + 1 > CalculateDaysInMonth(month)): #если меняется месяц
    if (month == 12): #если меняется год
        year += 1
        month = 1
    else:
        month += 1
    day = 1
else:
    day += 1

print(f'{day}-{month}-{year}')
