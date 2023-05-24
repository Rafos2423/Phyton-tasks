import time
from functools import wraps


total_time = 0

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global total_time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time += (end_time - start_time)
        return result
    return wrapper



def time_it_cached(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Время работы функции fibonacci cached: {end_time - start_time}")
            return result
        except Exception as ex:
            print(f"Работа функции прекращена из-за непредвиденной ошибки: {str(ex)}")
    return wrapper


def fibonacci_cache(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        if not cache:
            for i in range(min(2, n+1)):
                cache[i] = i

        for i in range(len(cache), n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]

    return wrapper


@time_it
def fibonacci(n):
    return n if n == 0 or n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


@time_it_cached
@fibonacci_cache
def fibonacci_cached(n):
    return n if n == 0 or n == 1 else fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print(fibonacci(20))
print(f"Время работы функции fibonacci: {total_time}")

print(fibonacci_cached(100000))
print(fibonacci_cached(100000))


