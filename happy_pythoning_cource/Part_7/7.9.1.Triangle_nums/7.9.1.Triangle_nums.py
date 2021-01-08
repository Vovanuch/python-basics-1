'''

Численный треугольник 3

Дано натуральное число nnn. Напишите программу, которая печатает численный треугольник с высотой равной nnn, в соответствии с примером:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.

Примечание. Используйте вложенный цикл for.

Sample Input:

3

Sample Output:

1
2 3
4 5 6

'''

n = int(input().strip())
count = 1
list_nums = []
start = 1
while True:
    a = list(range(start, start + count))
    list_nums.append(a)
    if len(list_nums) == n:
        break
    start += count 
    count += 1
    
for a in list_nums:
    print(*a)