#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased

print('Try to write into test2.txt file.')
with open('test2.txt', 'w') as fw1:
    x = 'My first line.\n'
    y = 'Second line!'
    fw1.write(x+y)


print()
print('Another writing with join method:')
with open('test3.txt', 'w+') as fw1:
    lines = [1, 2, 3, 4, 5]
    # In lambda-function we transform int to str 
    text = '\n'.join(map(lambda x: str(x), lines))
    fw1.write(text)

