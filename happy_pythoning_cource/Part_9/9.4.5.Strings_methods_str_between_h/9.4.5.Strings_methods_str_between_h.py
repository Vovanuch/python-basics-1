'''

Удаление фрагмента

На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

ahahahahaha

Sample Output 1:

aa

Sample Input 2:

hh

Sample Output 2:

'''

def get_list_of_indexes(my_list, char):
    list_of_indexes = []
    for i in range(len(my_list)):
        if my_list[i] == char:
            list_of_indexes.append(i)
    return list_of_indexes
            

s = input().strip()
list_chars = list(s)
char = 'h'
list_h_indexes = get_list_of_indexes(list_chars, char)

if len(list_h_indexes) > 1:
    s_new = s[:list_h_indexes[0]] + s[list_h_indexes[-1]+1:]

print(s_new)