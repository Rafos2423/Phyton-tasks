import random

def birthday(coltime, count_people):
    b_days = []
    count_true = 0

    for k in range(coltime):

        for i in range(count_people):
            d = str(f'{random.randint(1, 28)} {random.randint(1, 12)}')
            if b_days.__contains__(d):
                count_true += 1
                break
            b_days.append(d)

        b_days.clear()
    return count_true / coltime * 100


statement1 = birthday(1000, 23)
count_pairs = 23 * (23 - 1) / 2
statement2 = count_pairs / (28 * 12) * 100

print('%.2f, %.2f' % (statement1, statement2))

if statement1 < statement2:
    print(True)
else:
    print(False)