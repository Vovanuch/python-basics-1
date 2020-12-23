'''

Размножение n-ок

Напишите программу, которая считывает целое положительное число n, n∈[1; 9]n, \, n \in [1; \, 9]n,n∈[1;9] и выводит значение числа n+nn‾+nnn‾n+\overline{nn}+\overline{nnn}n+nn+nnn.

Формат входных данных
На вход программе подаётся одно целое положительное число n, n∈[1; 9]n, \, n \in [1; \, 9]n,n∈[1;9].

Формат выходных данных
Программа должна вывести число n+nn‾+nnn‾n+\overline{nn}+\overline{nnn}n+nn+nnn.

Примечание. Для первого теста 1+11+111=1231 + 11 + 111 = 1231+11+111=123.

Sample Input 1:

1

Sample Output 1:

123

Sample Input 2:

2

Sample Output 2:

246

Sample Input 3:

3

Sample Output 3:

369

'''

n = input().strip()
s = int(n) + int(2*n) + int(3*n)
print(s)