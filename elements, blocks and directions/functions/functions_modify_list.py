'''

Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.


'''

def modify_list(l):
	indx = []
	for i in range(len(l)):
		if (l[i] % 2 != 0):
			indx.append(i)
		if (l[i] % 2 == 0):
			l[i] = l[i] // 2
	indx.reverse()

	for j in indx:
		del l[j]	
			


li = [1, 2, 3, 4, 5, 6, 7]
modify_list(li)
print(li)
modify_list(li)
print(li)
'''
for i in l:
	#p = l.index(i)
	#print(p)
	if i % 2 == 1:
		l.remove(i)

print(l)

'''
