'''
той задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''


import requests
import json

def get_dict_from_file(file_name):
    my_dict = dict()
    with open(file_name, 'r') as inf:
        lines = inf.readlines()
        for line in lines:
            my_dict[line.strip()] = "Boring"
    return my_dict

def set_list_to_file(file_name, my_list):
    with open(file_name, 'w') as ouf:
        for i in my_list:
            ouf.write(i+'\n')
        

def get_answer_from_numbersapi(my_int):
    url = f"http://numbersapi.com/{my_int}/math?json=true"
    res = requests.get(url)
    data = res.json() 
    return data

def choose_interesting_or_boring_type(my_dict):
    for k in my_dict.keys():
        data = get_answer_from_numbersapi(k)
        if data['found'] == True:
            my_dict[k] = 'Interesting'
    return my_dict

def print_values(my_dict):
    for v in my_dict.values():
        print(v)
        
def get_values_as_a_list(my_dict):
    my_list = []
    for v in my_dict.values():
        my_list.append(v)
    return my_list


dict_int = dict()
dict_int = get_dict_from_file("dataset_24476_3.txt")
    
dict_int = choose_interesting_or_boring_type(dict_int)
print_values(dict_int)
list_types = get_values_as_a_list(dict_int)

set_list_to_file("dataset_answers.txt", list_types)

#print()
#print(dict_int)
