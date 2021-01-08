# Заполнение списков. Примеры.


a = [1] * 5
print(a)

b = [ 1 for i in range(4)]
print(b)


c = [i**2 for i in range(5)]
print(c)

d = [i for i in input().split()]
print(d)
