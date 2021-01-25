'''

Суммы двух

На вход программе подается натуральное число n≥2n \ge 2n≥2, а затем nnn целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (000 и 111, 111 и 222, 222 и 333 и т.д.).

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из сумм соседних чисел.

Sample Input 1:

5
1
2
3
4
5

Sample Output 1:

[3, 5, 7, 9]

Sample Input 2:

2
10
9

Sample Output 2:

[19]

'''

n = int(input().strip())
list_numbers = []
list_sums = []

# input n int numbers
for i in range(n):
    list_numbers.append(int(input().strip()))

# create list of summs
for i in range(n-1):
    list_sums.append(list_numbers[i] + list_numbers[i+1])
    
print(list_sums)