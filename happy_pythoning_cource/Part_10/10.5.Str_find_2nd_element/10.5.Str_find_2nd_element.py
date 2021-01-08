'''

Второе вхождение

На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

affective

Sample Output 1:

2

Sample Input 2:

python

Sample Output 2:

-2

Sample Input 3:

father

Sample Output 3:

-1

'''

s = input()
char = 'f'
count_f = 0
count_f = s.count(char)
if count_f == 0:
    res = -2
elif count_f == 1:
    res = -1
else:
    res = s.find(char, s.find(char) + 1)
print(res)