import time


def time_it(func):
    start_time = time.time()
    result = func(100)
    end_time = time.time()
    print(f"Время работы функции {func.__name__}: {end_time - start_time} секунд")
    return result


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


@time_it
@fibonacci_cache
def fibonacci_cached(n):
    return n if n == 0 or n == 1 else fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print(fibonacci(30))
print(fibonacci_cached(30))
print(fibonacci_cached(40))