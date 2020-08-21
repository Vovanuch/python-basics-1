#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_chetn(k, m=2):
    if k % m == 0:
        return True
    else:
        return False
        
my_list = [1, 2, 3, 4, 5]

# в новый список передаём только чётные, отфильтровываем
my_filter = filter(is_chetn, my_list)
print(f'Type of my_filter is {type(my_filter)}')
print(*my_filter)

print()
my_filtered_list = list(filter(is_chetn, my_list))

print ('filtered list is ', my_filtered_list)
