#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased

'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
'''

with open('dataset_24465_4.txt') as f, open('result.txt', 'w') as w:
    x = f.readlines()
    #print(x)
    x.reverse()
    #x = reversed(x)
    #print(x)
    result = ''.join(x)
    w.write(result)
    
