'''

Remove outliers

При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.

На вход программе подается натуральное число nnn, а затем nnn различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input:

10
9
17
189
3
55
78
11
7
888
160

Sample Output:

9
17
189
55
78
11
7
160

'''

n = int(input().strip())
list_numbers = []

# create list from input
for i in range(n):
    list_numbers.append(int(input().strip()))

#1st way
#del list_numbers[list_numbers.index(max(list_numbers))]
#del list_numbers[list_numbers.index(min(list_numbers))]

# 2nd way:
list_numbers.remove(max(list_numbers))
list_numbers.remove(min(list_numbers))

print(*list_numbers, sep='\n')