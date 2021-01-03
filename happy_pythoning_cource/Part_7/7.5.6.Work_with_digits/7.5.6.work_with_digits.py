'''

Все вместе

Дано натуральное число. Напишите программу, которая вычисляет:

    сумму его цифр;
    количество цифр в нем;
    произведение его цифр;
    среднее арифметическое его цифр;
    его первую цифру;
    сумму его первой и последней цифры.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

Sample Input 1:

5678

Sample Output 1:

26
4
1680
6.5
5
13

Sample Input 2:

132

Sample Output 2:

6
3
6
2.0
1
3

Sample Input 3:

75

Sample Output 3:

12
2
35
6.0
7
12

'''
'''
    сумму его цифр;
    количество цифр в нем;
    произведение его цифр;
    среднее арифметическое его цифр;
    его первую цифру;
    сумму его первой и последней цифры.
'''

def sum_digit(list_n):
    return sum(list_n)

def count_digit(n):
    return len(list_n)    

def multiply_digit(list_n):
    p = 1
    for i in list_n:
        p *= i
    return p  

def arifm_average_digit(list_n):
    aad = sum(list_n) / len(list_n)
    return aad

def first_digit(list_n):
    return list_n[0]

def sum_first_last_digit(list_n):
    return (list_n[0] + list_n[-1])


n = input().strip()
list_n = [int(i) for i in list(n)]


print(sum_digit(list_n))

print(count_digit(n))
print(multiply_digit(list_n))
print(arifm_average_digit(list_n))
print(first_digit(list_n))
print(sum_first_last_digit(list_n))
