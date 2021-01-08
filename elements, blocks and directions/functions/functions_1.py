''' фннкции
'''

def min2(a, b):
	if a <= b:
		return a
	else:
		return b
print('Enter 1st number')	
x = int(input())
print('Enter 2nd number')
y = int(input())
print('Min number is:', min2(x, y))

print('Три числа, поиск минимума:')
print(min2(43, min2(34, 40)))
