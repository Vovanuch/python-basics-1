# Двумерные массивы как списки списков. Заполнение.
 
n = 3
a = [[0] * n] * n
 
print(a)

a[0][0] = 5
# Неожиданно выводится 5,0,0 5,0,0 5,0,0 (три пятёрки вместо одной) потому, что второй и третий список ссылаются на первый список, на одну область памяти
print(a)

# Герераторы двумерных массивов:
print('\n b:')
b = [[1] * n for i in range(n)]
print(b)


print('\n c:')
c = [[2 * j for j in range(n)] for i in range(n)]
print(c)

# Здесь получается одномерный массив. ЗАполняем суммой индексов.
d = []
for i in range(n):
	for j in range(n):
		d.append(i + j)
		print(i + j, end=' ')
	print()
print(d)

# А здесь заполняем двумерный массив
print('\nЗаполняем двумерный массив')
m = []
x = 3
y = 4
z = 0

for i in range(x):
	m.append([])
	for j in range(y):
		m[i].append(z)
		z += 1
print(m)

print('\n')
# Красивый вывод двумерного массива:
for i in range(len(m)):
	for j in range(len(m[i])):
		print( m[i][j], end = ' ')
	print()


# Другой способ красивого вывода:
print('\n')
for row in m:
	for elem in row:
		print(elem, end = ' ')
	print()




'''



a = 3
b = 5
r = 0  # Чтобы было, чем заполнять
mas = []
for i in range(a):
    mas.append([])
    for j in range(b):
        mas[i].append(r)
        r += 1  # Чтобы заполнялось не одно и тоже

print(mas)
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]


'''
