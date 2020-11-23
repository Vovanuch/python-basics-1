'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv

'''


import csv
import collections

def get_primary_types_2015_from_csv_file(filename, mode, structure):
    with open(filename, mode) as f:
        reader = csv.reader(f)
        for r in reader:
            if r[2][6:10] == "2015":
                structure.append(r[5]) 

list_of_primary_types_2015 = []

get_primary_types_2015_from_csv_file('Crimes.csv','r',list_of_primary_types_2015)
finded_type = collections.Counter(list_of_primary_types_2015).most_common(1)
print('Most common crime is: ', finded_type[0][0])
print(f'It appears {finded_type[0][1]} times')
