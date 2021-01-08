#import itertools
from random import random 
from itertools import takewhile

def gen():
    x = 0
    while True:
        x = x + random()
        yield(x)
        

#print(list((itertools.takewhile(lambda y: y < 10, gen()))))
print(list((takewhile(lambda y: y < 3, gen()))))
