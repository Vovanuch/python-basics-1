'''

Одинаковые цифры

Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

Sample Input 1:

11111

Sample Output 1:

YES

Sample Input 2:

11112111

Sample Output 2:

NO

'''
n = input().strip()
if (len(set(n)) == 1):
    print('YES')
else:
    print('NO')