'''

Без нулей

Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести произведение отличных от нуля чисел.

Примечание. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.

Sample Input 1:

8
0
1
2
1
0
0
5
4
12

Sample Output 1:

3840

Sample Input 2:

1
43
2
234
78
0
1
1
23
4

Sample Output 2:

144409824

Sample Input 3:

3
8
66
1110
4
2
2
1
0
0

Sample Output 3:

28131840

'''
list_n = []

for _ in range(0, 10):
    list_n.append(int(input().strip()))
    
p = 1
for i in list_n:
    if i != 0:
        p *= i
        
print(p)