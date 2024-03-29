'''

Хороший оттенок

На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.

Примечание. Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.

Sample Input 1:

я очень хороший текст =)

Sample Output 1:

YES

Sample Input 2:

оыралоывало ХОРОШвмсва выарлво83кг834

Sample Output 2:

YES

Sample Input 3:

Цвет настроения синий

Sample Output 3:

NO

'''

s = input().strip()
n = 'хорош'

if n in s.lower():
    print('YES')
else:
    print('NO')