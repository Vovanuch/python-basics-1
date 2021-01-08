'''

Таблица-2

Дано натуральное число n  (n≤ 9)n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5n \times 5n×5, где в iii-ой строке указано число iii (числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n×5n \times 5n×5 в соответствии с условием.

Примечание. В конце строки может быть пробел.

Sample Input 1:

3

Sample Output 1:

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3

Sample Input 2:

6

Sample Output 2:

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
6 6 6 6 6

Sample Input 3:

1

Sample Output 3:

1 1 1 1 1

'''


def get_str_from_sumb(a, n):
    s = a
    for _ in range(n-1):
        s += ' ' + a
    
    return s

s = input().strip()
for i in range(1, int(s)+1):
    s_long = get_str_from_sumb(str(i), 5)
    print(s_long)