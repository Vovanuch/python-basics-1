'''

Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.



Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:

3 21 22
10 6 19
20 16 -1

Sample Input 2:

1
end

Sample Output 2:

4


'''
end = ''
# массив строк, получаемый из ввода
strm = []
# массив сумм чисел
sm = []
# массив чисел, получаемый из строк
m = []

while end != 'end':
	s = input()
	if s != 'end':
		strm.append(s)
	else:
		break

#j = 0
for i in strm:
	m.append(i.split())
	sm.append([])

for i in range(len(m)):
	for j in range(len(m[i])):
		m[i][j] = int(m[i][j])	
		sm[i].append(0)



for i in range(len(m)):
	
	for j in range(len(m[i])):
		

		# m[i % len(m)][j % len(m[i])] - база
		sm[i][j] = m[(i-1) % len(m)][j % len(m[i])] +  m[(i + 1) % len(m)][j % len(m[i])] +  m[i % len(m)][(j - 1) % len(m[i])] +  m[i % len(m)][(j + 1) % len(m[i])]
	
	
			
			
for i in range(len(sm)):
	for j in range(len(sm[i])):
		print(sm[i][j], end =' ')

	print()
