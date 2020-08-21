#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_list = [1, 2, 3, 4]
my_dic = {"author":"Afanasyev", "book_series":"Doctor", "book_name":"Doctor. Nachalo" }
my_str = "Amazing book!"

my_list_of_lists = [my_list, my_dic, my_str]

for i in my_list_of_lists:
    print("\nNew list, see it! Welcome!")
    for j in i:
        print(j, end = " ")

# ---------
print()
print('Lets see all lists:')
iterator_dic = iter(my_dic)
print(next(iterator_dic))
print(next(iterator_dic))
print(next(iterator_dic))
#print(next(iterator_dic))

# ---------

it = iter(my_list)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
