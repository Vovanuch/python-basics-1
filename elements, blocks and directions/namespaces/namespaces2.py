'''



Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

    create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует

Рассмотрим набор запросов

    add global a
    create foo global
    add foo b
    create bar foo
    add bar a

Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен, созданной при выполнении данного кода

a = 0
def foo():
  b = 1
  def bar():
    a = 2

В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. Далее мы объявляем функцию foo, что влечет за собой создание локального для нее пространства имен внутри пространства global. В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo функцию bar, тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.

Добавим запросы get к нашим запросам

    get foo a
    get foo c
    get bar a
    get bar b

Представим как это могло бы выглядеть в коде

a = 0
def foo():
  b = 1
  get(a)
  get(c)
  def bar():
    a = 2
    get(a)
    get(b)

Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a, но в пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.

Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве global не была объявлена переменная с.

Более формально, результатом работы get <namespace> <var> является

    <namespace>, если в пространстве <namespace> была объявлена переменная <var>
    get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
    None, если не существует <parent>, т. е. <namespace>﻿ – это global

Формат входных данных

В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.
Формат выходных данных

Для каждого запроса get выведите в отдельной строке его результат.


Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output:

global
None
bar
foo



'''
'''
# Мой комментарий на форуме Степика.
Дааа. Задача выела мозг, конечно.

Первоначально, без подсмотра в комментарии, реализовывал вариант с двумя словарями, dic_namespaces, где хранится текущий неймспейс и его родитель, и dic_variables, где ключ - неймспейс, а значение - массив переменных. Sample intup решал нормально, правдиво и без подгона.) Но тесты проходил только 7 из 31.

Второй раз, почитав умных людей в комментах, решил использовать вложенные словари.

namespaces={ 'global': {'parent': None, 'vars': []}, }

Помогло.

Реализацию сделал через две функции: одна запускает команды, сохранённые в листе листов

def run_list(command_list):

Другая ищет неймспейс переменной по переданному имени и текущему неймспейсу.

def find_ns(var, ns):

В этой функции главный словарь словарей namespaces объявлен как global

Надеюсь, поможет разобраться и найти правильный путь. :)

'''    



''' функция поиска неймспейса у переменной '''
def find_ns(var, ns):
    global namespaces
    #print()
    #print(f'namespaces inside find_ns function. Var = {var}, ns = {ns}')
    #print( f'namespaces[ns][\'vars\']:',namespaces[ns]['vars']) 
    tmp_lst_var = namespaces[ns]['vars'] 
    #print(f'try to find var {var} in list {tmp_lst_var}')  
    if var in tmp_lst_var:
        return ns
    else:
        #print(f'We didnt find var {var} in list {tmp_lst_var}. Lets go to parent namespase. Feel the light side power!) ')
        if ns != 'global':
            return find_ns(var, namespaces[ns]['parent'])
        else:
            #print('We didnt find any namespase. None is a result')
            return 'None'



''' функция запуска команд из списка строк'''
def run_list(command_list):
    global namespaces
    #print()
    #print('namespaces inside run_list')
    #print(namespaces)
    for line in command_list:
        if line[0] == 'create':
            namespaces[line[1]] = {'parent': line[2], 'vars': []}
            #print('namespaces inside run_list when create new ns:')
            #print(namespaces)
        elif line[0] == 'add':
            namespaces[line[1]]['vars'].append(line[2])
            #print('namespaces inside run_list when add new variable:')
            #print(namespaces)            
        elif line[0] == 'get':
            #print(f'go into find_ns with params: var = {line[2]}, namespace = {line[1]}')
            print(find_ns(line[2], line[1]))



#namespace_input.txt
command_list = []

n = int(input())
for i in range(n):
    command_list.append(input().strip().split())




'''
#Вводим данные из файла namespace_input.txt
tmp_list = []
with open('namespace_input.txt') as inf:
    for line in inf:
        tmp_list.append(line.strip())
        
n = int(tmp_list[0])



#создаём список из строк, содержащий команды и  аргументы
for i in range(1, len(tmp_list)):
    command_list.append(tmp_list[i].strip().split())

print(command_list)
'''

#Тестовый список 1
#tst1 = [['add', 'global', 'a'], ['create', 'foo', 'global'], ['add', 'foo', 'b'], ['get', 'foo', 'a'], ['get', 'foo', 'c'], ['create', 'bar', 'foo'], ['add', 'bar', 'a'], ['get', 'bar', 'a'], ['get', 'bar', 'b']]
#Тестовый список 2
'''
test2 = [['add', 'global', 'a'], ['create', 'foo', 'global'], ['add', 'foo', 'b'],
        ['get', 'foo', 'a'], ['get', 'foo', 'c'], ['create', 'bar', 'foo'], ['add', 'bar', 'a'],
        ['get', 'bar', 'a'], ['get', 'bar', 'b']]  
'''

#Словарь словарейб где ключ - неймспейс, значение - словарь, состоящий из родителя и переменных
namespaces={ 'global': {'parent': None, 'vars': []}, }

#command_list = tst1
#print('command list:')
#print(*command_list)
#print()
#print('namespaces:')
#print(namespaces)


run_list(command_list)

#print()
#print(namespaces)
