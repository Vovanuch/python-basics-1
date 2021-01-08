'''

Переворот

На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

abch12345h

Sample Output 1:

abch54321h

Sample Input 2:

qwertyhasdfghzxcvb

Sample Output 2:

qwertyhgfdsahzxcvb

'''

s = input().strip()
str_part = s[s.find('h')+1 : s.rfind('h')]
s_new = s[:s.find('h')] + str_part + s[s.rfind('h')+1:]

print(s_new)