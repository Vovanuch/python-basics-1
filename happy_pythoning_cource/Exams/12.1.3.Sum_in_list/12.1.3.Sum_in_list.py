'''

Сумма чисел

На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.

Формат выходных данных
Программа должна текст в соответствии с условием задачи.

Примечание. Строковый метод join() работает только со списком строк.

Sample Input 1:

2 5 11 33 55

Sample Output 1:

2+5+11+33+55=106

Sample Input 2:

1 1 1

Sample Output 2:

1+1+1=3

'''

list_nums = input().strip().split()
list_nums = [int(i) for i in list_nums]
print(*list_nums, sep='+', end='')
print('=', sum(list_nums), sep='')