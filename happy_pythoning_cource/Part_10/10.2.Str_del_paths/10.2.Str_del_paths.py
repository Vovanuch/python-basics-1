'''

Каждый третий

На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы, кратные 3, то есть символы с индексами 0, 3, 6, ....

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести строку текста в соответствии с условием задачи.

Sample Input:

Python

Sample Output:

yton

'''
s = input().strip()
s_new = ''
for i in range(len(s)):
    if i % 3 != 0:
        s_new += s[i]
print(s_new)