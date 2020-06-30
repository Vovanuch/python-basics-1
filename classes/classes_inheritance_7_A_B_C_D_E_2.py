''' class inheritance '''
class A:
    pass
    
class B(A):
    pass
        
        
class C:
    pass
    
class D(C):
    pass

# class E(B, C, D) - ошибка! НЕльзя наследовать и "сына", и "отца" - C и D
# class E(B, D) - можно
# class E(B, C) - можно
class E(B, C, D):
    pass

    
#print(E.mro()) - это тоже работающий вызов
print(E.__mro__)

my = E()
