# Поиск минимума.
# Можно воспользоваться стандартной функцией min, а можно написать самому ))

a = [int(i) for i in input().split()]
#print(a)
mini = a[0]
for i in a:
	if i < mini:
		mini = i
print(mini)
