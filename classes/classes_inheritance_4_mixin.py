''' Classes. Mixin '''
class EvenMixin:
    def even_length(self):
        return (len(self) % 2) == 0
        
class MyList(list, EvenMixin):
    pass
    
class MyDict(dict, EvenMixin):
    pass    

print('mro для MyList:')
print(MyList.mro())
x = MyList([1, 2, 3, 4, 5])
print(*x)
print('Длина моего списка чётная? ', x.even_length())
x.append(6)
x.extend([7, 8])
print(*x)
print('Длина моего списка чётная? ', x.even_length())


print()
print('mro для MyDict:')
print(MyDict.mro())
d = MyDict({1: 'a', 2: 'b', 3: 'c'})
print(d)
print('Длина моего словаря чётная? ', d.even_length())
d[4] = 'd'
print(d)
print('Длина моего словаря чётная? ', d.even_length())
