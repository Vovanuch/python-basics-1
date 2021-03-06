'''

Наибольшее и наименьшее

Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

Формат входных данных
На вход программе подается пять целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.

Sample Input 1:

1
2
3
4
5

Sample Output 1:

Наименьшее число = 1
Наибольшее число = 5

Sample Input 2:

454
453
32
8
6769

Sample Output 2:

Наименьшее число = 8
Наибольшее число = 6769

Sample Input 3:

-3
-11
-499
-888
0

Sample Output 3:

Наименьшее число = -888
Наибольшее число = 0

'''
nums = []
for i in range(5):
    nums.append(int(input().strip()))
    
print(f'Наименьшее число = {min(nums)}')
print(f'Наибольшее число = {max(nums)}')