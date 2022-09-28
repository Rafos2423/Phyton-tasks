lst = [int(s) for s in input().split()]

for i in range(len(lst)):
    if (i + 1) % 2 == 1:
        print(lst[i])