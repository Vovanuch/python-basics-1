''' Classes. Method resolution order '''

class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

print('Порядок разрешения методов для класса А:')
print(A.mro())
