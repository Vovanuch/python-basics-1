'''

Сумма двух списков

На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 символ пробел.

Формат входных данных
На вход программе подаются две строки текста, содержащие целые числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Количество чисел в обоих строках одинаковое.

Sample Input 1:

3 1 4
1 5 9

Sample Output 1:

4 6 13

Sample Input 2:

1 1 1 1 1 1
9 9 9 9 9 9

Sample Output 2:

10 10 10 10 10 10

'''
def get_list_numbers(string):
    list_nums = string.strip().split()
    list_nums = [int(i) for i in list_nums]
    return list_nums

list_numbers_1 = get_list_numbers(input())
#print(list_numbers_1)
list_numbers_2 = get_list_numbers(input())
#print(list_numbers_2)
list_numbers_3 = [list_numbers_1[i] + list_numbers_2[i] for i in range(len(list_numbers_1))]

print(*list_numbers_3)
