'''

Первое и последнее вхождение

На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке, разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

abcdefg

Sample Output 1:

5

Sample Input 2:

abcdefgfhfabc

Sample Output 2:

5 9

Sample Input 3:

abcd

Sample Output 3:

NO

'''

s = input().strip()
symbol = 'f'
count = 0
list_indexes = []
for i in range(len(s)):
    if s[i] == symbol:
        list_indexes.append(i)
        
if len(list_indexes) == 0:
    print('NO')
elif len(list_indexes) == 1:
    print(*list_indexes)
else:
    print(list_indexes[0], list_indexes[-1])
