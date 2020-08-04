''' iterators and generatiors 5'''

from random import random

def random_generator():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    yield 2
    print('Checkpoint 3')
    

gen = random_generator()
x = next(gen)
print('x =', x)
y = next(gen)
print('y =', y)

z = next(gen) # StopIteration exception
#print('z =', z)
