'''

Перестановка цифр

Дано трехзначное число abc‾\overline{abc}abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке: abc, acb, bac, bca, cab, cbaabc, \, acb, \, bac, \, bca, \, cab, \, cbaabc,acb,bac,bca,cab,cba.

Sample Input 1:

123

Sample Output 1:

123
132
213
231
312
321

Sample Input 2:

987

Sample Output 2:

987
978
897
879
798
789

'''

n = input().strip()
list_n = list(n)
list_results = []

s = list_n[0] + list_n[1] + list_n[2]
list_results.append(s)
s = list_n[0] + list_n[2] + list_n[1]
list_results.append(s)
s = list_n[1] + list_n[0] + list_n[2]
list_results.append(s)
s = list_n[1] + list_n[2] + list_n[0]
list_results.append(s)
s = list_n[2] + list_n[0] + list_n[1]
list_results.append(s)
s = list_n[2] + list_n[1] + list_n[0]
list_results.append(s)

for i in list_results:
    print(i)