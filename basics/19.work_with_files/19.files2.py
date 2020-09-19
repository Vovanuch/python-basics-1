#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r - read
# w - write (old data losed when writing)
# a - appenf, write to end of file 
# b - binary
# r+ - read and write to end
# W+ - read and write, data is erased






# 2nd way to open

with open("test2.txt", "w+") as f2:
    f2.write("new line No ")
print ("2nd file created")


print('f3')
with open("test.txt", "r+") as f3:
    x = f3.read()
    x = x.splitlines()
    print(x*2)


#print()
#print()
print()

print('f4')
with open("test.txt", "r+") as f4:
    list_of_rows = f4.readlines()
    #list_of_rows = list_of_rows
    for line in list_of_rows:
        #print(line)
        print(line.strip())
        line = line.strip()
    
    #print(list_of_rows)

print()
print('f5')
with open("test.txt", "r+") as f5:
    x = f5.read()
    x = x.splitlines()
    print('x as a filepointer:')
    print(repr(x))
    print()
    print('printing in array:')
    for row in x:
        print(row)



print()
print('f6')
with open("test.txt", "r+") as f6:
    for line in f6:
        print('str:', str(line))
        print('repr:', repr(line))
