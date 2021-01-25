'''

Сумма цифр

Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

Sample Input 1:

12345

Sample Output 1:

15

Sample Input 2:

12

Sample Output 2:

3

Sample Input 3:

7

Sample Output 3:

7

'''

# объявление функции
def print_digit_sum(num):
    s = 0
    for n in num:
        s += int(n)
    print(s)

# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)