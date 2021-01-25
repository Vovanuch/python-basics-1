'''

Удалите нечетные индексы

На вход программе подается натуральное число nnn, а затем nnn целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список в соответствии с условием задачи.

Примечание. Используйте оператор del.

Sample Input 1:

10
0
1
2
3
4
5
6
7
8
9

Sample Output 1:

[0, 2, 4, 6, 8]

Sample Input 2:

1
8

Sample Output 2:

[8]

Sample Input 3:

2
9
6

Sample Output 3:

[9]

'''

n = int(input().strip())
list_numbers = []

# create list from input
for i in range(n):
    list_numbers.append(int(input().strip()))

# delete odd positions (indexes)    
for i in range(n-1, 0, -1):
    if i % 2 != 0:
        del list_numbers[i]
        
print(list_numbers)