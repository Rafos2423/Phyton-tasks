month = int(input())

if (month == 2):
    print(28)
elif (month < 8):
    if (month % 2 == 1):
        print(31)
    else:
        print(30)
else:
    if (month % 2 == 1):
        print(30)
    else:
        print(31)