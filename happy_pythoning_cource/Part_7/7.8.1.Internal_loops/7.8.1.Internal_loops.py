'''

Таблица-1

Дано натуральное число n  (n≤ 9)n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3n \times 3n×3 состоящую из данного числа (числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n×3n \times 3n×3 состоящую из данного числа.

Примечание. В конце строки может быть пробел.

Sample Input 1:

8

Sample Output 1:

8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8
8 8 8

Sample Input 2:

4

Sample Output 2:

4 4 4
4 4 4
4 4 4
4 4 4

Sample Input 3:

1

Sample Output 3:

1 1 1

'''
def get_str_from_sumb(a, n):
    s = a
    for _ in range(n-1):
        s += ' ' + a
    
    return s

s = input().strip()
s_long = get_str_from_sumb(s, 3)
for i in range(int(s)):
    print(s_long)