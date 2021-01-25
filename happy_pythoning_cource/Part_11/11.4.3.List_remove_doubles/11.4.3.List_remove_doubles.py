'''

Без дубликатов

На вход программе подается натуральное число nnn, а затем nnn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.

Sample Input:

5
first
second
first
third
second

Sample Output:

first
second
third

'''

n = int(input().strip())
lisr_rows = []
lisr_rows_no_doubles = []

# create list from input
for i in range(n):
    lisr_rows.append(input().strip())
    
for s in lisr_rows:
    if s not in lisr_rows_no_doubles:
        lisr_rows_no_doubles.append(s)
    
print(*lisr_rows_no_doubles, sep='\n')