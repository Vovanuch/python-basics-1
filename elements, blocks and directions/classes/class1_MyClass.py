''' Классы. Начало. '''

class MyClass:
    a = 10
    
    def func(self=None):
        print('Hello from MyClass!')

print(MyClass.a)
print(MyClass.func())

print()
mc = MyClass()
mc.func()
print(f'mc type is {type(mc)}' )
print(f'MyClass type is {type(MyClass)}' )
