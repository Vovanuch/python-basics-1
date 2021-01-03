'''

Цвет настроения синий

Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

Какой хороший день!

Sample Output 1:

NO

Sample Input 2:

Как называется этот красивый синий камень в Вашем кольце?

Sample Output 2:

YES

Sample Input 3:

Разглядите синий густой цвет.

Sample Output 3:

YES

'''

s = input().strip()
if 'синий' in s:
    print('YES')
else:
    print('NO')
    
