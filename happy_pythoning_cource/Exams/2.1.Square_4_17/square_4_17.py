'''
Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*).

Примечание. Высота и ширина прямоугольника равны 444 и 171717 звёздочкам соответственно.

Sample Input:

Sample Output:

*****************
*               *
*               *
*****************

'''

def print_squar(lis):
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            print(lis[i][j], end='')
        print()


a = 4
b = 17
list_n = [[' '] * b for i in range(a)]

for i in range(b):
    list_n[0][i] = '*'
    list_n[3][i] = '*'

list_n[1][0] = '*'
list_n[2][0] = '*'
list_n[1][16] = '*'
list_n[2][16] = '*'


print_squar(list_n)