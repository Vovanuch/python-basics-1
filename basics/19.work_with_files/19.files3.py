#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased

print()
print('f7')
with open("test.txt", "r+") as f7:
    # manually show 1st and 2nd rows
    x = f7.readline().strip()
    print(x)
    x = f7.readline().strip()
    print(x)
    #print(repr(x))
    
print()
print('f8')
with open("test.txt", "r+") as f8:    
    y = f8.readlines()
    print('Raw list with full unstripped strings: \n', y)
    
    print()
    for i in range(len(y)):
        y[i] = y[i].strip()
        
    print('List with stripped rows from file: \n', y)
    
