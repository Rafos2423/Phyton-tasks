import time


def time_it(func):
    start_time = time.time()
    result = func(1000000)
    end_time = time.time()
    print(f"Время работы функции {func.__name__}: {end_time - start_time}")
    return result


@time_it
def even_numbers_append(n):
    even_list = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


@time_it
def even_numbers_comprehension(n):
    even_list = [i for i in range(n + 1) if i % 2 == 0]
    return even_list
