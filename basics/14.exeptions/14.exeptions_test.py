dic = {'a':'', 'b':'a', 'c':'b', 'd':'', 'e':'a'}
lst = ['a', 'b', 'c', 'd']

for ex in lst:
    print(ex, lst.index(ex))

a = []
for i in range(10):
    a.append(i)
    
print(*a)

for i in a:
    print(i, a.index(i))
    for j in range( a.index(i), len(a)):
        print(a[j])

