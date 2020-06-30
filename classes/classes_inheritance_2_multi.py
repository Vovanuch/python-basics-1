''' Classes. Subclass '''

class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

x = A()
print('Is x an instance of A?', isinstance(x, A))
print('Is x an instance of B?', isinstance(x, B))
print('Is x an instance of C?', isinstance(x, C))
print('Is x an instance of D?', isinstance(x, D))
print('Is x an instance of E?', isinstance(x, E))
print('Is x an instance of object?', isinstance(x, object))
print('Is x an instance of string?', isinstance(x, str))
print('Is x an instance of list?', isinstance(x, list))
