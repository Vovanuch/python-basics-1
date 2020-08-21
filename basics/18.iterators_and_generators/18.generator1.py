#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random


def random_gemerator(k):
    for i in range(k):
        yield random()

my_var = random_gemerator(3)
print(type(my_var))

for v in my_var:
    print(v)
