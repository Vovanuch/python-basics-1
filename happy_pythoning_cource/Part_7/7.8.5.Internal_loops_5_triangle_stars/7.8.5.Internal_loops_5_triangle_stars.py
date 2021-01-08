'''

Звездный треугольник 🌶️🌶️

Дано нечетное натуральное число nnn. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным nnn в соответствии с примером:

*
**
***
****
***
**
*

Формат входных данных
На вход программе подается одно нечетное натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.

Sample Input 1:

3

Sample Output 1:

*
**
*

Sample Input 2:

5

Sample Output 2:

*
**
***
**
*

'''
def print_star_row(n):
    print('*' * n)

def print_star_row_up(m, n):
    for i in range(m, n+1):
        print_star_row(i)
        
def print_star_row_down(m, n):
    for i in range(m, n-1, -1):
        print_star_row(i)


n = int(input().strip())
print_star_row_up(1, n // 2)
print_star_row_down((n // 2) + 1, 1)

