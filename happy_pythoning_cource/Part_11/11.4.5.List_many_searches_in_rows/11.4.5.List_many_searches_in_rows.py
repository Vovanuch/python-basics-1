'''

Google search - 2 🌶️🌶️

На вход программе подается натуральное число nnn, затем nnn строк, затем число kkk — количество поисковых запросов, затем kkk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

Формат входных данных
На вход программе подаются натуральное число nnn — количество строк, затем сами строки в указанном количестве, затем число kkk, затем сами поисковые запросы.

Формат выходных данных
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

Примечание. Поиск не должен быть чувствителен к регистру символов.

Sample Input:

5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
2
язык
python

Sample Output:

Язык Python прекрасен
язык Python появился 20 февраля 1991

'''

def get_search_results(my_list, search):
    list_search_results = []
    for row in my_list:
        if search.lower() in row.lower():
            list_search_results.append(row)
    return list_search_results


# list of rows
list_rows = []

# what we want to search
list_searches = []
# list of results
list_search_result = []
list_search_result_another = []

# count of rows
n = int(input().strip())
# create list from input
for i in range(n):
    list_rows.append(input().strip())

# count of searches
k = int(input().strip())
# create list of searches from input
for i in range(k):
    list_searches.append(input().strip())


# make a search for all requests
for search in list_searches:
    res = get_search_results(list_rows, search)
    #print(f'Search fo {search} is {res}')
    list_search_result.extend(res)
    #list_search_result_another.append(res)
    #print(list_search_result_another)

list_search_result_strong = []
for i in list_search_result:
    if (list_search_result.count(i) == k) and (i not in list_search_result_strong):
        list_search_result_strong.append(i)

print(*list_search_result_strong, sep='\n')

'''    
# create list with strong intersection
if k > 1:
    list_search_result_strong = [elem for elem in list_search_result if (list_search_result.count(elem) > 1)]
    #list_search_result_strong = list(set(list_search_result_strong))
    list_search_result_strong_2 = [elem for elem in list_rows if elem in list_search_result_strong]
    
else:
    list_search_result_strong_2 = list_search_result

print(*list_search_result_strong_2, sep='\n')
'''