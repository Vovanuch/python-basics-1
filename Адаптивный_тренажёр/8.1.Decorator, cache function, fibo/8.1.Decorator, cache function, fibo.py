# decorators
# cache function

from functools import lru_cache
# Числа Фибоначчи (попробуйте убрать lru_cache) :)

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(100)])
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...]
print(fib.cache_info())
#CacheInfo(hits=196, misses=100, maxsize=None, currsize=100)