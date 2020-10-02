'''
How we use operator package
'''


import operator as op

# using math functions and others from operator package 
print(op.add(4, 5))
print(op.mul(3, 6))


a = [1, 2, 3, 4, 5, 6, 10]
print(op.contains(a, 3))

op.delitem(a, 1) # del 2
print(a)

b = op.getitem(a, 1) # b = 3
print('Get a[1]:', b)

print('Index of 4 in a:', op.indexOf(a, 4))

fun1 = op.itemgetter(2, 3)
print('Use itemgetter:', fun1(a))

d1 = {'asd': 3, "qwer": 4}
fun2 = op.itemgetter('asd')
print('itemgetter for dictionary: get value by sending key to itemgetter.', fun2(d1))