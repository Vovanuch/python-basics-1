'''

До КОНЦА 1

На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек). Напишите программу, которая выводит члены данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести члены данной последовательности.

Sample Input 1:

Fus
Ro
КОНЕЦ
Dah

Sample Output 1:

Fus
Ro

Sample Input 2:

По
небу
полуночи
КОНЕЦ
ангел
летел

Sample Output 2:

По
небу
полуночи

Sample Input 3:

Dead
by
Daylight
КОНЕЦ
Good Game

Sample Output 3:

Dead
by
Daylight

'''
text = input().strip()
while text != 'КОНЕЦ':
    print(text)
    text = input().strip()
