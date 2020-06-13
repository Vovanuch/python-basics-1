''' function printing a, b'''
def printab(a, b):
    print(a)
    print(b)
    
#few ways to call a function
printab(50, 'gramm')
print()
printab(a='30', b = 'seconds')
#equal as
printab(b = 'seconds', a='30')

print()
printab(10, b = '20 mins')
'''error! multiple args for a. 10 and 20 mins both'''
#printab(10, a = '20 mins')

print()
lst = [1, 2]
printab(*lst) # == printab(lst[0], lst[1])
print('')
printab(lst[0], lst[1])

print()
args = {'a': 100, 'b': 200}
printab(*args) # a, b
printab(**args) ## 100, 200

print()

