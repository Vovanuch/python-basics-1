''' стэк вызовов  '''

def f1():
    print('It\'s the f1 function.')

def g1():
    print('Now it is the g1 function.')
    f1()
    print('Now it is the g1 function.')

print('Outside of any function..')
f1()
g1()
f1()
print('Outside of any function..')
