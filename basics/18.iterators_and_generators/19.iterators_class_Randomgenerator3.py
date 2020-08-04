''' iterators and generatiors 3'''

from random import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random() # random values from 0 to 1
        else:
            raise StopIteration

n = 5

for x in RandomIterator(n):
    print(x)
