#!/usr/bin/env python3
# -*- coding: utf-8 -*-


list1 = [1, 2, 3, 4, 5]
print('list1 = ', list1)

list2 = list(map(lambda x: x*2, list1))
print('mapped list2 = ', list2)
