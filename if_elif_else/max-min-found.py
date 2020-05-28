"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""
x = int(input())
y = int(input())
z = int(input())
# max and min founded with standart functions
#ma = max(x, y, z)
#mi = min(x, y, z)

#2nd way to fin max and min
#max
if (x >= y) and (x >= z):
	ma = x
elif (y >= x) and (y >= z):
	ma = y
elif (z >= y) and (z >= x):
	ma = z

#min
if (x <= y) and (x <= z):
	mi = x
elif (y <= x) and (y <= z):
	mi = y
elif (z <= y) and (z <= x):
	mi = z


#printing block

if (x == ma) and (y == mi):
	print(x)
	print(y)
	print(z)
elif (x == ma) and (z == mi):
	print(x)
	print(z)
	print(y)
	
elif (y == ma) and (z == mi):
	print(y)
	print(z)
	print(x)
	
elif (y == ma) and (x == mi):
	print(y)
	print(x)
	print(z)

elif (z == ma) and (x == mi):
	print(z)
	print(x)
	print(y)
	
elif (z == ma) and (y == mi):
	print(z)
	print(y)
	print(x)


