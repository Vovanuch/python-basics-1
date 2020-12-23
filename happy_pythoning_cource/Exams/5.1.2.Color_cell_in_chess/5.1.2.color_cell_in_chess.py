'''

Шахматная доска

Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

1
1
2
6

Sample Output 1:

YES

Sample Input 2:

2
2
2
5

Sample Output 2:

NO

'''


points = [0, 0, 0, 0]
for i in range(4):
    points[i] = int(input().strip())
    
if ((points[0] + points[1])%2 == (points[2] + points[3])%2):
    print('YES')
else:
    print('NO')