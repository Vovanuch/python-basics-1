'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv

'''

import csv

def get_2015_from_csv_file(filename, mode, structure):
    with open(filename, mode) as f:
        print("Current file:")
        reader = csv.reader(f)
        for r in reader:
            if r[2][6:10] == "2015":
                structure.append(r) 

def get_primary_types(structure, set_of_types):
    for s in structure:
        if (s[5]) and (s[5] not in set_of_types):
            set_of_types.add(s[5])
        
def fill_dict_of_types(my_set, my_dict):        
    for s in my_set:
        my_dict[s] = 0
        
def get_count_of_types(structure, dict_of_collection):
    for line in structure:
        dict_of_collection[line[5]] = dict_of_collection[line[5]] + 1
        
def dict_print(my_dict):        
    for k, v in my_dict.items():
        print(k, v)

def get_all_primary_types(structure, my_list):
    for s in structure:
        my_list.append(s[5])
            
def get_uniq_primary_types(my_set, my_list): 
    my_set = set(my_list)
    return my_set
            
def get_dict_of_primary_types_and_count(my_list, my_set, my_dict):
    for s in my_set:
        my_dict[s] = my_list.count(s)

def get_key_of_max_element_in_dict(my_dict):
    #my_max = max(my_dict.values())
    key = max(my_dict, key=my_dict.get)
    return key
            
list_common_2015 = []
list_of_primary_types = []
set_of_primary_types = set()
dict_of_primary_types = dict()

get_2015_from_csv_file("Crimes.csv", "r", list_common_2015)
get_all_primary_types(list_common_2015, list_of_primary_types)
set_of_primary_types = get_uniq_primary_types(set_of_primary_types, list_of_primary_types)
get_dict_of_primary_types_and_count(list_of_primary_types, set_of_primary_types, dict_of_primary_types)
dict_print(dict_of_primary_types)

print(f'\nMost common type of crime is {get_key_of_max_element_in_dict(dict_of_primary_types)}')

#print(list_of_primary_types)
#print(set_of_primary_types)

#get_primary_types(list_common_2015, set_of_primary_types)
#fill_dict_of_types(set_of_primary_types, dict_of_primary_types)
#get_count_of_types(list_common_2015 ,dict_of_primary_types)
#dict_print(dict_of_primary_types)
    
#print("\n\n\n")


    
#print(max(dict_of_primary_types.values()))
# max_val = max(scores, key=scores.get)
#finded_type = max(dict_of_primary_types, key=dict_of_primary_types.get)
#print(finded_type)