#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# using generator
print('using generator for power 2')
list1 = list(i**2 for i in range(6))

print(list1)

# using filter and lambda for values [1:14] 
print('using filter and lambda for values [1:14] ')
print(*filter(lambda x: x>0 and x < 15, list1))


# generator 2
print()
print('using generator for power 2 with condition % 2 == 0')
list2 = list(i**2 for i in range(1, 11) if i % 2 == 0)

print(list2)
