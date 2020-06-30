''' Classes. Переопределение функций '''
class EvenMixin:
    def even_length(self):
        return (len(self) % 2) == 0
        
class MyList(list, EvenMixin):
    def pop(self):
        x = super(MyList, self).pop()
        print(f'last value is {x}')
        return x
        
x = MyList([1, 2, 3])
print('x is:', *x)
x.pop()
print('Now x is:', *x)
