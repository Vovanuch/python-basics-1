'''
Змеиный регистр

Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:

this_is_camel_cased
is_prime_number

'''

# объявление функции
def convert_to_python_case(text):
    list_symbols = list(text)
    for i in range(len(list_symbols)):
        if 'A' <= list_symbols[i] <= 'Z':
            list_symbols[i] = list_symbols[i].lower()
            if i != 0:
                list_symbols.insert(i, '_')
    return ''.join(list_symbols)

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))