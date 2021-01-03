'''

Арифметические строки

Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

Sample Input 1:

abc
a
abcde

Sample Output 1:

YES

Sample Input 2:

2434
90099
21

Sample Output 2:

NO

Sample Input 3:

aaaaaaaaaa10
1111111Nm
22222r

Sample Output 3:

YES

'''

cits = {}

for i in range(3):
    a = input().strip()
    cits[a] = len(a)
    
list_len = sorted(cits.values())

if ((list_len[1] - list_len[0]) == (list_len[2] - list_len[1])):
    print("YES")
else:
    print('NO')
    