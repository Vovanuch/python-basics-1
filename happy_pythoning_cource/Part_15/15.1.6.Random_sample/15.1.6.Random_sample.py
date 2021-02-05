'''
Функция sample()

Функция sample() принимает два обязательных аргумента: список (строку) и количество случайных элементов, а возвращает список случайных элементов в указанном количестве.

Результатом работы кода:

import random
 
numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))

может быть:

[9]
[12, 5]
[9, 2, 8]
[12, 8, 9, 5, 2]
'''

import random

n = [1, 2, 3, 6, 8, 9, 0, 11, 15, 13]
print(random.sample(n, 1))
print(random.sample(n, 3))
print(random.sample(n, 6))
