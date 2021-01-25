'''

Список кубов

На вход программе подается натуральное число nnn, а затем nnn целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из кубов указанных чисел.

Sample Input 1:

5
1
2
3
4
5

Sample Output 1:

[1, 8, 27, 64, 125]

Sample Input 2:

2
-5
-2

Sample Output 2:

[-125, -8]

Sample Input 3:

1
100

Sample Output 3:

[1000000]

'''

n = int(input().strip())
list_nums = []
list_cubes = []
for _ in range(n):
    list_nums.append(int(input().strip()))
list_cubes = [i**3 for i in list_nums]
print(list_cubes)