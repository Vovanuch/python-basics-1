'''

Ход слона 🌶️

Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный слон ходит по диагоналям.

Sample Input 1:

4
4
5
5

Sample Output 1:

YES

Sample Input 2:

4
4
5
4

Sample Output 2:

NO

Sample Input 3:

4
4
5
3

Sample Output 3:

YES

'''

points = [0, 0, 0, 0]
for i in range(4):
    points[i] = int(input().strip())
'''    
if ((points[0]+points[1]) == (points[2]+points[3])) or (abs(points[1]-points[0]) == abs(points[3]-points[2])):
    print('YES')
else:
    print('NO')
'''    
#'''    
d1 = abs(points[0] - points[1])
d2 = abs(points[2] - points[3])

d3 = abs(points[0] + points[1])
d4 = abs(points[2] + points[3])

d5 = abs(points[3] - points[1])
d6 = abs(points[2] - points[0])



if (d3 == d4) or (d5 == d6):
    print('YES')
else:
    print('NO')
#'''