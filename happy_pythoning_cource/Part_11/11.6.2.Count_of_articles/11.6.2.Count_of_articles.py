'''

Количество артиклей

На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

Формат входных данных
На вход программе подается строка, содержащая английский текст. Слова текста разделены символом пробела.

Формат выходных данных
Программа должна вывести общее количество артиклей 'a', 'an', 'the' вместе с поясняющим текстом.

Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.

Sample Input:

William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.

Sample Output:

Общее количество артиклей: 7

'''
list_articles = ['a', 'an', 'the']
text = input().strip().lower()
#print(text)
list_words = text.split()
#print(list_words)
count = 0

#print(list_articles.count('a'))
#print(list_articles.count('an'))
#print(list_articles.count('the'))

for a in list_articles:
    count += list_words.count(a)

print(f'Общее количество артиклей: {count}')
