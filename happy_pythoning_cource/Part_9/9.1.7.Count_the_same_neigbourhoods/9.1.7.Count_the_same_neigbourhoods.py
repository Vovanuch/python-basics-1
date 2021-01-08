'''

Одинаковые соседи

На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество одинаковых соседних символов.

Sample Input 1:

abcd

Sample Output 1:

0

Sample Input 2:

aabbcc

Sample Output 2:

3

Sample Input 3:

aaa

Sample Output 3:

2

'''

n = input().strip()
count = 0
for i in range(len(n) - 1):
    if n[i] == n[i+1]:
        count += 1
print(count)