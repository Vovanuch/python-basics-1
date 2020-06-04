x = 4
y = x
print('x =', x)
print('y =', y)
print('Are y and x links to the same memory?', (y is x))
print('id(x) =', id(x))
print('id(y) =', id(y))

print()
print('now x became 5')
x += 1
y = int(10/2)
print('x =', x)
print('y =', y)
print('Are y and x still links to the same memory now?', (y is x))
print('id(x) =', id(x))
print('id(y) =', id(y))

print()
xx = [1, 2, 3]
print('id(xx) =',id(xx))
print('id of list =', id([1, 2, 3]))

print()
x = [1, 2, 3, 4]
y = x
print('x =', x)
print('y =', y)
print('id(x) =', id(x))
print('id(y) =', id(y))

x.append(5)
print('Are y and x still links to the same memory now?', (y is x))
print('x =', x)
print('y =', y)
print('id(x) =', id(x))
print('id(y) =', id(y))

''' равенство значений и неравенство идентификаторов. Списки'''
print()
x = [1, 2, 3]
y = x
print('y is [1, 2, 3]?', y is [1, 2, 3])
print('y == [1, 2, 3]?', y == [1, 2, 3])

print()

''' сиписки и строки 2'''

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)
