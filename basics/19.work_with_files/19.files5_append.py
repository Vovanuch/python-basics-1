#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased

print('Try to write to file with a attribute.')
with open('test_append.txt', 'a') as fapp:
    s = 'Moscow never sleep... \n'
    fapp.write(s)
    print('We did it!')


print()
print('Try to append to exactly that file.')
with open('test_append.txt', 'a') as fapp:
    fapp.write('\nThe tired toys are sleeping now... \n')
    print('Oooops, we did it again! (c) old-old woman)))')
