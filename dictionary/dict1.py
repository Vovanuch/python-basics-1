# Dictionary. Словари
d1 = dict()

d2 = {}

d3 = {'a':100, 'b':"Boris", 'abc':[10, 20, 30]}

print()
print('Keys in d3:')
print(*d3)
#a b abc
print()
for x in d3:
	print(x, 'is a key,  ', d3[x], 'is a value')

print('То же самое:')
for x in d3.keys():
	print(x, d3[x])
	

# key in dictionary
# key not in dictionary

#dictionary[key] = value - добавить или перезаписать
d3['a'] = 200
print('new value of key \'a\' is', d3['a']) 

#dictionary[key] - если такого ключа нет, то возникнет ошибка.
# Для безопасного получения используем функцию get(). dictionary.get(key)
print('b is', d3.get('b'))
#ключа c нет, поэтому None
print('c is', d3.get('c'))

# del dictionary[key] - удаляем всю пару, ключ-значение
del d3['b']
print(*d3)
# добавляем
d3['f'] = 'function'
print(*d3)

# ключи уникальны и неизменяемы! Элементы не имеют порядка
# Ключами не могут быть списки и другие словари

print()
for value in d3.values():
	print(value, end=' ')
	
print()
for key, value in d3.items():
	print(key, value)
