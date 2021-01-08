'''

Напишите программу, которая считывает список чисел lst lst lst из первой строки и число x x x из второй строки, которая выводит все позиции, на которых встречается число x x x в переданном списке lst lst lst.

Позиции нумеруются с нуля, если число x x x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:

5 8 2 7 8 8 2 4
8

Sample Output 1:

1 4 5

Sample Input 2:

5 8 2 7 8 8 2 4
10

Sample Output 2:

Отсутствует

'''


lst = []
lstind = []
for i in input().split():
	lst.append(int(i))
	
x = int(input())

for i in range(len(lst)):
	if lst[i] == x:
		lstind.append(i)

if len(lstind) > 0:
	print(*lstind)
else:
	print("Отсутствует")
