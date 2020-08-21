#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#test
#соответственно

import sys


for i in range(5):
    print(5)

print(sys.version_info)

n = 1554
str_next = f'The next number for the number {n} is {n+1}.'
str_prev = f'The previous number for the number {n} is {n-1}.'
print(str_next)
print(str_prev)



students_class = []
table_class = []

for i in range(3):
    students_class.append(int(input()))
    table_class.append(0)

for i in range(3):
    table_class[i] = (students_class[i] // 2) + (students_class[i] % 2)
    print(table_class[i])
