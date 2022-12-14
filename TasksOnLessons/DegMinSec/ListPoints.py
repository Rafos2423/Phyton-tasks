import task3
from random import randint as ra_int

def get_coord():
    a = ra_int(100000, 360 * 100000)
    return a / 100000

def create_list(*args, **kwargs):
    result = []
    countPoint = 0
    for i in args:
        countPoint += 1
        result.append(f'point {countPoint} = {task3.deg_to_gms(i)}')
    for k, v in kwargs.items():
        result.append(f'{k} = {task3.deg_to_gms(i)}')

    return result

print(*create_list(get_coord(), get_coord(), get_coord(), get_coord(), pole = get_coord(), put_1 = get_coord()), sep = "\n")