'''
shuffle


Функция shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.

Следующий код перемешивает список numbers случайным образом, а затем выводит его содержимое:

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

Результатом работы такого кода может быть:

[4, 7, 8, 1, 2, 3, 6, 5]
'''
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(numbers)
print(numbers)