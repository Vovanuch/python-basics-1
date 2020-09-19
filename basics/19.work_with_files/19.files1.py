#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased

# 1st way to open file
f = open('test.txt', 'r+')

for i in range(5):
    f.write(f'{i+1} row here.\n')

print("file is completed!")  

f.write ("\nThis is the end of file!")
f.close()



f = open('test.txt', 'r')
# в скобках - количество символов
x = f.read(30)
print('x = ', x)

print('repr(x) = ', repr(x))

print()
y = f.read()
print(y)

f.close()
