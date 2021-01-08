#!/usr/bin/env python3
# -*- coding: utf-8 -*-


mylist = [1, 2, 3]
print(mylist)
print('3 in list?', 3 in mylist)
print('3 in list?', 3 in mylist)

my_generated_list = list(num**2 for num in mylist)
print(my_generated_list)

print(list(my_generated_list))
print(list(my_generated_list))


# without type list()

my_generated_list = (num**2 for num in mylist)
print(my_generated_list)

print(list(my_generated_list))
print(list(my_generated_list)) # this will be empty


print()
numbers = [1,2,3,4,5]
a,b, *rest = numbers
print(rest)
print(*rest)
