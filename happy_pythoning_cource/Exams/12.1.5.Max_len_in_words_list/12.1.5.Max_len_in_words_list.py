'''

Самый длинный

На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input:

проспал почти всю ночь

Sample Output:

7

'''
list_words = input().strip().split()
list_len_words = [len(word) for word in list_words]
print(max(list_len_words))