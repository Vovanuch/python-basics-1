'''

Переставить min и max

На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

Формат входных данных
На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести строку текста в соответствии с условием задачи.

Примечание. Используйте подходящие встроенные функции и списочные методы.

Sample Input 1:

3 4 5 2 1

Sample Output 1:

3 4 1 2 5

Sample Input 2:

10 9 8 7 6 5 4 3 2 1

Sample Output 2:

1 9 8 7 6 5 4 3 2 10

Sample Input 3:

1 2

Sample Output 3:

2 1

Sample Input 4:

1

Sample Output 4:

1

'''

list_strings = input().strip().split()
list_numbers = [int(i) for i in list_strings]

index_max = list_numbers.index(max(list_numbers))
index_min = list_numbers.index(min(list_numbers))

list_numbers[index_max], list_numbers[index_min] = list_numbers[index_min], list_numbers[index_max] 
print(*list_numbers)