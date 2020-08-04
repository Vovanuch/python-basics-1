''' iterators and generatiors 2'''

from random import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
    
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random() # random values from 0 to 1
        else:
            raise StopIteration

n = 4

x = RandomIterator(4)

for i in range(n+1):
    #при n+1 - на последнюю итерацию будер ругаться.
    print(next(x)) #next(x) == x.__next__()
