#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased

with open('test2.txt') as f, open('test4.txt', 'w') as w:
    for line in f:
        w.write(line)
    print('We make a copy of file2 to file 4.')
