''' iterators and generatiors 4'''

from random import random

def random_generator(k):
    for i in range(k):
        yield random()

n = 10
gen = random_generator(n)
print(f'Type of gen is {type(gen)}')

for i in gen:
    print(i)
