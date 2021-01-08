'''


Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d d d известных нам слов, после чего на d d d строках указываются эти слова. Затем передаётся количество l l l строк текста для проверки, после чего l l l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the



'''

ngloss = int(input())
gloss = set()
words= []
setwords = ()
errors = set()

for i in range(ngloss):
	gloss.add(input().strip().lower())

#print('glossary')
#print(*gloss)

nwords = int(input())

for i in range(nwords):
	words += (input().strip().lower().split())
#print('words:')
#print(*words)

setwords = set(words)
#print('setwords:')
#print(*setwords)


for word in setwords:
	if word not in gloss:
		errors.add(word)
		
#print('err:')
for err in errors:
	print(err)

