''' iterators and generatiors 1'''

from random import random

class RandomIterator:
    def __next__(self):
        return random() # random values from 0 to 1
    
x = RandomIterator()
print(next(x)) #next(x) == x.__next__()
