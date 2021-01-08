'''

Выведите таблицу размером n×n n \times n n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5 n=5 n=5):

Sample Input:

5

Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9



'''

n = int(input())
m = [[0 for i in range(n)] for j in range(n)]
ind = [[0 for i in range(n)] for j in range(n)]


'''
for i in m:
	for j in i:
		print(j, end = ' ')
	print()


m1 = []
for i in range(1, n**2+1):
	m1.append(i)
print (*m1)
'''


x, y = 0, 0
dx, dy = 1, 0


	
for i in range(1, n**2 + 1):
	m[x][y] = i
	nx, ny = x+dx, y+dy
	if (0 <= nx < n) and (0 <= ny < n) and (m[nx][ny] == 0):
		x, y = nx, ny
	else:
		dx, dy = -dy, dx
		x, y = x+dx, y+dy		
		
for x in list(zip(*m)):
	print(*x)		
	
'''
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[j][i], end=" ")
    print()
'''	
	
