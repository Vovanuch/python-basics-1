'''

Последовательность символов

Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:

AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G

Формат входных данных

Формат выходных данных
Программа должна вывести указанную последовательность символов.

Sample Input:

Sample Output:

AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G

'''

lis = ['AAA', 'BBBB', 'E', 'TTTTT', 'G']

for i in range(6):
    print(lis[0])

for i in range(5):
    print(lis[1])

print(lis[2])

for i in range(9):
    print(lis[3])

print(lis[4])