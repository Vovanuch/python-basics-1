'''

Координатные четверти

Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.

Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – xxx, затем ордината – yyy), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.

Sample Input 1:

4
0 -1
1 2
0 9
-9 -5

Sample Output 1:

Первая четверть: 1
Вторая четверть: 0
Третья четверть: 1
Четвертая четверть: 0

Sample Input 2:

10
4 8
-3 -1
-4 9
4 0
-4 0
5 -2
0 0
1 1
13 -3
-43 3

Sample Output 2:

Первая четверть: 2
Вторая четверть: 2
Третья четверть: 1
Четвертая четверть: 2

'''
def list_to_int(my_list):
    #for c in my_list:
    return list(map(int, my_list))   

#a1, a2, a3, a4 = 0, 0 ,0 , 0
quatro_count = [0] * 4
quatro_lines = []



point_count = int(input())
point_coords = []
for i in range(point_count):
    point_coords.append(list_to_int(input().split()))
    

for point in point_coords:    
    if point[0] > 0:
        if point[1] > 0:
            quatro_count[0] += 1
        elif point[1] < 0:
            quatro_count[3] += 1
    elif point[0] < 0:
        if point[1] > 0:
            quatro_count[1] += 1
        elif point[1] < 0:
            quatro_count[2] += 1
            

quatro_lines.append(f"Первая четверть: {quatro_count[0]}")
quatro_lines.append(f"Вторая четверть: {quatro_count[1]}")
quatro_lines.append(f"Третья четверть: {quatro_count[2]}")
quatro_lines.append(f"Четвертая четверть: {quatro_count[3]}")

for line in quatro_lines:
    print(line)