''' iterators and generatiors 6'''

from random import random

def random_generator():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    
    return "This is the end!"
    # тут мы обрубаем исполнение, до yield 2 уже никогда не дойдём
    
    yield 2
    print('Checkpoint 3')
    
    

gen = random_generator()
x = next(gen)
print('x =', x)
y = next(gen)
print('y =', y)

z = next(gen) # StopIteration exception
