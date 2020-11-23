'''
factorial error
'''

def f(n=5):
    while n > 1:
        return n * int(f(n-1))

print(f(3))