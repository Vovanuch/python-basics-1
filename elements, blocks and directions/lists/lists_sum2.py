'''

Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:

1 3 5 6 10

Sample Output 1:

13 6 9 15 7

Sample Input 2:

10

Sample Output 2:

10

'''

a = [int(i) for i in input().split()]
l = len(a)
b = []
b0 = 0
bn = 0
#print(l)

if l > 1:
	b0 = a[1] + a[l-1]
	b.append(b0)
	
	
	for i in range(1,l-1):
		bi = a[i-1] + a[i+1]
		b.append(bi)

	
	bn = a[l-2] + a[0]	
	b.append(bn)
elif l == 1:
	b = a

for i in b:
	print(i, end = ' ')
