'''
test function
'''

def f(x=1, y=2):
    x = x + y
    y = y + 1
    return(x, y)

print(f(y=2, x=1))