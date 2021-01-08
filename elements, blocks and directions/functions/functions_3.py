# поиск минимума с произвольным кол-вом параметров

def min3(*a):
	if len(a) > 0:
		m = a[0]
		for i in a:
			if m > i:
				m = i
		return(m)
	else:
		return()
		
arr = input().split()
for i in arr:
	i = int(i)
	
print(min3(*arr))
