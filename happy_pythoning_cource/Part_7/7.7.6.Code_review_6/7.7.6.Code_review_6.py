'''

Ревью кода-6

На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа. Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 333). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
'''

p = 1

n = input().strip()

list_n = [int(i) for i in list(n) if i.isdigit()]
for i in list_n:
    p *= i
print(p)