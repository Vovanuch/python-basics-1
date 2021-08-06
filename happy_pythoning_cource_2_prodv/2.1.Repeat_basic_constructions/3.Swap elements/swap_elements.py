'''

Назад, вперёд и наоборот

На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). Если в списке нечетное количество элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.

Sample Input 1:

1 2 3 4 5

Sample Output 1:

2 1 4 3 5

Sample Input 2:

2 3 2 4

Sample Output 2:

3 2 4 2

Sample Input 3:

1

Sample Output 3:

1

'''

my_list = list(map(int, input().split()))

for i in range(1, len(my_list), 2):
    my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
    
print(*my_list)