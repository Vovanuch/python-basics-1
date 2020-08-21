#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import takewhile
from itertools import count
import itertools

'''
Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя.
Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел.
Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1.

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

Пример использования:

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

'''
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def primes():
    cnt = 2
    while True:
        if is_prime(cnt):
            yield cnt
        cnt += 1
        
    
    

print(list(itertools.takewhile(lambda x : x <= 231, primes())))
