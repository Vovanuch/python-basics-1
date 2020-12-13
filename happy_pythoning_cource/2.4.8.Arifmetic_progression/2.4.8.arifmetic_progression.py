'''

Арифметическая прогрессия

Арифметической прогрессией называется последовательность чисел a1,a2,...,an a_1, a_2, ..., a_n a1​,a2​,...,an​, каждое из которых, начиная с a2 a_2 a2​, получается из предыдущего прибавлением к нему одного и того же постоянного числа d d d (разность прогрессии), то есть:

an=an−1+da_n=a_{n−1}+dan​=an−1​+d

Если известен первый член прогрессии и её разность, то n n n-ый член арифметической прогрессии находится по формуле:

an=a1+d(n−1)a_n=a_1+d(n-1)an​=a1​+d(n−1)

Входные данные
На вход программе подаётся три целых числа: a1 a_1 a1​, d d d и n n n, каждое на отдельной строке.

Выходные данные
Программа должна вывести n n n-ый член арифметической прогрессии.

Sample Input 1:

1
1
10

Sample Output 1:

10

Sample Input 2:

-1
1
2

Sample Output 2:

0

Sample Input 3:

100
50
1

Sample Output 3:

100

'''
list_n = []
list_base = []
for i in range(3):
    list_base.append(int(input().strip()))
list_n.append(list_base[0])

res = 0
for i in range(1, list_base[2]):
    list_n.append(list_n[i-1] + list_base[1])
    
#print(*list_n)
print(list_n[len(list_n) - 1])