'''


Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:

class Error1(Error2, Error3 ... ErrorK):
    pass


Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.

Формат входных данных

В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.
Формат выходных данных

Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.
Пример теста 1

Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")


...



По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError можно не ловить, в
едь мы уже ловим OSError -- предок FileNotFoundError

Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:

FileNotFoundError



'''
#функция формирования словаря из класса
def make_dic_from_lst(lst_classes, dic_classes):
    for cls in lst_classes:
        if len(cls) == 1:
            dic_classes[cls[0]] = ''
        else:
            dic_classes[cls[0]] = cls[2:]
    return dic_classes



#функция поиска пути пежду двумя элементами из словаря - проверка, является ли второй родителем для первого. 
#возвращает путь от первого ко второму.
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
    

def find_unwanted(dic_classes, lst_in):
    lst_out = []
    for ex in lst_in:
        curr_index = lst_in.index(ex)
        for i in range(curr_index+1, m):
            tmp_lst = find_path(dic_classes, ex, lst_in[i])
            if tmp_lst:
                #print(f'{ex} compares with {lst_reversed_exceptions[i]}: {lst_reversed_exceptions[i]} is parent!')
                lst_out.append(ex)
                #print(f'{ex}, {lst_in.index(ex)}')
                break
            #else:
                #print(f'For {ex} and {lst_reversed_exceptions[i]} are no relatives!')
                
    return lst_out
    
    


lst_classes = []
lst_exceptions = []
dic_classes  = {}

my_ban_set = set()

n = int(input())
for i in range(n):
    lst_classes.append(input().strip().split())

m = int(input())
for i in range(m):
    lst_exceptions.append(input().strip())
    
#print()
#print('Entered data:')
#print('classes:', *lst_classes)
#print('exceptions:', *lst_exceptions)


# формируем словарь классов из введённого на основе списка
#print('Make dictionary from list:')
dic_classes = make_dic_from_lst(lst_classes, dic_classes)
#print(dic_classes)

#переворачиваем список исключений в обратном порядке
lst_reversed_exceptions = list(reversed(lst_exceptions))

#print('Reversed exceptions:', *lst_reversed_exceptions)
#print('Current exceptions:', *lst_exceptions)

#curr_len = len(lst_exceptions)

my_lst_unwanted = find_unwanted(dic_classes, lst_reversed_exceptions)
#print(*my_lst_unwanted)
my_lst_unwanted = list(dict.fromkeys(my_lst_unwanted))
#print('remove duples:', *my_lst_unwanted)
my_lst_unwanted_rev = reversed(my_lst_unwanted)
#print('Reverced dedupled list:', *my_lst_unwanted_rev)

for i in my_lst_unwanted_rev:
    print(i)

'''
for ex in lst_reversed_exceptions:
    curr_index = lst_reversed_exceptions.index(ex)
    #print(ex, curr_index)
    
    for i in range(curr_index+1, m):
        tmp_lst = find_path(dic_classes, ex, lst_reversed_exceptions[i])
        if tmp_lst:
            #print(f'{ex} compares with {lst_reversed_exceptions[i]}: {lst_reversed_exceptions[i]} is parent!')
            print(f'{ex}')
        #else:
            #print(f'For {ex} and {lst_reversed_exceptions[i]} are no relatives!')
'''

