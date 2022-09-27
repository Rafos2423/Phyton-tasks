import random
a = [0, 0, 1]
count = 0
for i in range(100000):
    choice = random.randint(0, 2)
    for i in range(2):
        if (a[i] == 0 and i != choice):
            choiseLead = i;
            break
    if (choice == 1):
        count += 1;

print(count/1000)



