''' class inheritance '''

class A:
    def foo(self):
        print('A')
        
class B(A):
    pass
    
class C(A):
    def foo(self):
        print('C')
        
class D:
    def foo(self):
        print('D')
        
class E(B, C, D):
    pass
    
my = E()
print(my.foo())
E().foo()
print(E.__mro__)

