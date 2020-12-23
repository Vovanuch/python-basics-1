'''

Пересечение отрезков 🌶️🌶️

На числовой прямой даны два отрезка: [a1;   b1][a_1; \,  b_1][a1​;  b1​] и [a2;  b2][a_2; \, b_2][a2​; b2​]. Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:

    отрезок;
    точка;
    пустое множество.

Формат входных данных
На вход программе подаются 4 целых числа a1, b1, a2, b2a_1, \, b_1, \, a_2, \, b_2a1​,b1​,a2​,b2​, каждое на отдельной строке. Гарантируется, что a1<b1a_1 < b_1a1​<b1​​ и a2<b2a_2 < b_2a2​<b2​​.

Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».

Sample Input 1:

1
3
2
4

Sample Output 1:

2 3

Sample Input 2:

1
2
3
4

Sample Output 2:

пустое множество

Sample Input 3:

5
6
6
8

Sample Output 3:

6

'''

a1 = int(input().strip())
b1 = int(input().strip())
a2 = int(input().strip())
b2 = int(input().strip())

list_1 = [i for i in range(a1, b1+1)]
list_2 = [i for i in range(a2, b2+1)]
list_3 = sorted(list(set(list_1 + list_2)))
list_common = []
for i in list_3:
    if i in list_1 and i in list_2:
        list_common.append(i)

#if not list_common:
#    print('пустое множество')

if len(list_common) >= 2:
    print(min(list_common), max(list_common))
elif len(list_common) == 1:
    print(*list_common)
elif len(list_common) == 0:
    print('пустое множество')
#print(*list_common)