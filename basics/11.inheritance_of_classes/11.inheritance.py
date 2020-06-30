'''


Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass



Класс A является предком класса B, если

    A = B;
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C


Например:

class B(A):
    pass

class C(B):
    pass

# A -- предок С



Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", 
если класс 1 является предком класса 2, и "No", если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A

Sample Output:

Yes
Yes
Yes
No


   '''
'''   
   
def check_class(dic_cls, parent, son):
      pass
      #for k, v in dic_cls.items():
      #if     

def make_full_classes(str_class, lst_parents=[]):
    if lst_parents == []:
        print(f'{str_class} is a parent class. Exit.')
        return
'''

'''        
def get_parent(cls_son, lst_par = []):
#    print('Function start: cls_son:', cls_son, 'lst_par:', *lst_par)
    if dic_classes[cls_son]:
#        print('START IF: dic_classes[cls_son]:', dic_classes[cls_son], 'cls_son:', cls_son, 'lst_par:', *lst_par)
        lst_par.extend(dic_classes[cls_son])
        lst_par = list(set(lst_par))
#        print('END IF: dic_classes[cls_son]:', dic_classes[cls_son], 'cls_son:', cls_son, 'lst_par:', *lst_par)
#        print(f'parents of {cls_son}:', *lst_par)
        #for par in lst_par:
        #    get_parent(par)
    else:
        lst_par = []
#        print('Else way: cls_son:', cls_son, 'lst_par:', *lst_par)
#        print(f'parents of {cls_son}: empty')
        
    return lst_par #dic_classes[cls_son]

#def get_parent2(cls):
'''
'''
def get_parent(son):
    tmp_lst = dic_classes[son]
    for i in tmp_lst:
        dic_classes_full[son].append(get_parent(i))
'''


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
    


    


lst_classes = []
lst_requests = []

dic_classes = {}
dic_classes_full = {}
dic_requests = {}
   
count_classes = int(input())
for i in range(count_classes):
    lst_classes.append(input().strip().split())
    

count_requests = int(input())
for i in range(count_requests):
    lst_requests.append(input().strip().split())

# формируем словарь классов из введённого на основе списка
for cls in lst_classes:
    if len(cls) == 1:
        dic_classes[cls[0]] = ''
    else:
        dic_classes[cls[0]] = cls[2:]




for req in lst_requests:
    tmp_lst = find_path(dic_classes, req[1], req[0])
    if tmp_lst:
        print('Yes')
        #print('Class-way is:', tmp_lst, 'points:',req[0], req[1])
    else:
        print('No')
        #print('Points:',req[1], req[0])





'''
# выводим на экран словарь классов
print('Entered classes dict:')
for k, v in dic_classes.items():
    print(k, v)
'''
    
'''    
# заполняем полный словарь dic_classes_full значениями из словаря dic_classes
for k in dic_classes.keys():
    dic_classes_full[k] = []
    dic_classes_full[k].extend(dic_classes[k])
'''

#for k, v in dic_classes_full.items():
#    get_parent(k)

# выводим на экран полный словарь
'''print('full classes dict:')
for k, v in dic_classes_full.items():
    print(k, v)
'''

#print('lst_requests is:', lst_requests)








#for req in lst_requests:
#    print(f'Parents of requested {req[0]} is', get_parent(req[0]))



#for k, v in dic_classes_full.items():
#    print(k, v)

#pars = []

#print('list of classes:', *lst_classes)
#print('list of requests:',*lst_requests)
#print()
#print(dic_classes)
#print(dic_requests)
