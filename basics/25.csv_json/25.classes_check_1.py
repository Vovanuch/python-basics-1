'''


Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass


Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2
'''


'''
Для тех кто отчаялся, тезисно:

    создаем функцию, которая возвращает всех потомков класса (и учесть сам класс)
    создать множество, в котором будут учтены всевозможные родители (помнить, что класс, от которого никто не наследуется, является родителем для себя самого)
    Отсортировать множество в лексикографическом порядке
    Вывести все имена из множества сопостовляя их с количеством потомков (см. п.1)

Кому и это не помогло, рекомендую отладить код по следующим входным данным:

inp = json.loads("""[{"name": "G", "parents": ["ZZZ"]}, 
                     {"name": "TH", "parents": ["ZZZ"]},
                     {"name": "G", "parents": ["ZY"]}, 
                     {"name": "G", "parents": ["F"]}, 
                     {"name": "A", "parents": []}, 
                     {"name": "B", "parents": ["A"]}, 
                     {"name": "C", "parents": ["A"]}, 
                     {"name": "D", "parents": ["B", "C"]},
                     {"name": "E", "parents": ["D"]}, 
                     {"name": "F", "parents": ["D"]}, 
                     {"name": "X", "parents": []},
                     {"name": "Y", "parents": ["X", "A"]},
                     {"name": "Z", "parents": ["X"]},
                     {"name": "V", "parents": ["Z", "Y"]},
                     {"name": "W", "parents": ["V"]}]""")

Корректный вывод

A : 10
B : 5
C : 5
D : 4
E : 1
F : 2
G : 1
TH : 1
V : 2
W : 1
X : 5
Y : 3
Z : 3
ZY : 2
ZZZ : 3

На самом деле,  у некоторых кто успешно справился с заданием, вывод с этими входными данными может быть некорректным, так как тут условия еще более жесткие: имена классов могут быть из 2-ух и более символов, некоторые классы родителей (ZZZ, ZY, TH и др.) упоминаются только в parents и для них не создан отдельный словарь, но их нужно учесть при выводе.
'''



'''
пробовал отловить ошибки по тестам в комментариях, проходил их все кроме одного ( ссылка на него https://stepik.org/lesson/24473/step/4?discussion=1074555&unit=6777), вот тест, пройдя который, я закрыл задание:

[{"name": "A", "parents": ["B", "C", "D"]},{"name": "E", "parents": ["F", "G"]},{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "B", "parents": ["I", "Y", "D", "G"]},{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]
A : 1
B : 2
C : 2
D : 9
E : 4
F : 5
G : 8
I : 3
Y : 9
Z : 7
'''



import json




def find_path(graph, start, end, path=[]):
    
    path = path + [start]

    if start == end:
        return path

    if not graph.__contains__(start):
        return None

    for node in graph[start]:

        if node not in path:

            newpath = find_path(graph, node, end, path)

            if newpath: return newpath

    return None    





classes_dict = dict()
classes_parents_dict = dict()
class_count_dict = dict()

classes_list = []

classes_set = set()

# load json data from file
'''
with open("25.classes.json", 'r') as inf:
    classes_dict = json.load(inf)
'''

# load json data from input
#'''
input_info = input()
classes_dict = json.loads(input_info)
#'''

# load json from string
'''
classes_dict = json.loads("""[{"name": "G", "parents": ["ZZZ"]}, 
                     {"name": "TH", "parents": ["ZZZ"]},
                     {"name": "G", "parents": ["ZY"]}, 
                     {"name": "G", "parents": ["F"]}, 
                     {"name": "A", "parents": []}, 
                     {"name": "B", "parents": ["A"]}, 
                     {"name": "C", "parents": ["A"]}, 
                     {"name": "D", "parents": ["B", "C"]},
                     {"name": "E", "parents": ["D"]}, 
                     {"name": "F", "parents": ["D"]}, 
                     {"name": "X", "parents": []},
                     {"name": "Y", "parents": ["X", "A"]},
                     {"name": "Z", "parents": ["X"]},
                     {"name": "V", "parents": ["Z", "Y"]},
                     {"name": "W", "parents": ["V"]}]""")
'''


# create full list of classes names 
for cls in classes_dict:
    classes_list.append(cls['name'])
    for c in cls['parents']:
        classes_list.append(c)

# create set of classes names
classes_set = set(classes_list)

# fill classes_parents_dict
for cls in classes_dict:
    #print(cls['name'], cls['parents'])
    classes_parents_dict[cls['name']] = cls['parents']

for s1 in classes_set:
    class_count_dict[s1] = 0
    
for s1 in classes_set:
    for s2 in classes_set:
        if find_path(classes_parents_dict, s2, s1):      
            #print(f'{s2} -> {s1}')
            class_count_dict[s1] += 1


# fill dict with values of counting (frequencies of elements)
'''
for cl in set(classes_list):
    class_count_dict[cl] = classes_list.count(cl)
'''


# print sorted view of dictionary with classes and frequencies
'''
for key in sorted(class_count_dict.keys()):
    print(f'{key} : {class_count_dict[key]}')
'''    
# 2nd way of printing dict, sorted by keys 
for elem in sorted(class_count_dict.items()):
    print(f'{elem[0]} : {elem[1]}')

#print('dict', classes_parents_dict)

#print('set', sorted(classes_set))


