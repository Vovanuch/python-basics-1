#!/usr/bin/env python3
# -*- coding: utf-8 -*-

base_list = [-2, -1, 0, 1, 2]
print(f'base_list: {base_list}')

# 1st, usual way
power_list1 = []
for x in base_list:
    power_list1.append(x ** 2)
print(f'1st power_list: {power_list1}')

# 2nd way, with generator
power_list2 = [i*i for i in base_list]
print(f'2nd power_list: {power_list2}')


# 3rd way, with generator and condition (if)
power_list3 = [i*i for i in base_list if i > -2]
print(f'3rd power_list with condition if: {power_list3}')


# 4th case. few  arguments and condition 
pair_list1 = [(a, b) for a in range(5) for b in range(5) if a < b]
print(f'pair_list1 is: {pair_list1}')

a = list(i+1 for i in range(4))
print(a)


a = [i for i in range(5)][1:]
print(a)
