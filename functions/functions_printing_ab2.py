''' function printing a, b : addition 2'''

def printab2(a, b, *args):
    print('Position arg a:', a)
    print('Position arg b:', b)
    print('Other args:')
    for arg in args:
        print(arg)


def printab3(*args):
    for arg in args:
        print(arg)    

def printab4(a, b, **args):
    print('Position arg a:', a)
    print('Position arg b:', b)
    print('Other args:')
#'''
#    for arg in args.items(): # это тоже работает, но попробуем и другой способ
#        print(arg[0], arg[1]) 
#'''
    for key in args:
        print(key, args[key])


lst = [1, 2, 3, 4, 5]
printab2(*lst)
print()


lst2 = [10, 20, 30]
printab3(*lst2)
print()

printab4(5, 10, aa=15, bb=20, cc=25, dd=30)
