'''

Алфавит

Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка состоит из 26 символов z.
'''

list_chars = []
for i in range(97, 97 + 26):
    list_chars.append(chr(i) * (i - 96))
    
print(list_chars)
    