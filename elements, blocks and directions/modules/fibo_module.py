#fibonacci module
import sys

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, b + a

def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, b + a
	return result
'''		
fib(10)
print()
m = fib2(100)
print(*m)
'''

if (__name__ == '__main__') and (len(sys.argv) > 1):
	
	fib(int(sys.argv[1]))
	
