'''

Три города

Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.

Sample Input 1:

Москва
Санкт-Петербург
Екатеринбург

Sample Output 1:

Москва
Санкт-Петербург

Sample Input 2:

Нью-Йорк
Вашингтон
Чикаго

Sample Output 2:

Чикаго
Вашингтон

Sample Input 3:

Париж
Марсель
Лион

Sample Output 3:

Лион
Марсель

'''

def get_key(my_dict, val):
    for k, v in my_dict.items():
        if v == val:
            return k
    return 'No such key for that value'

cits = {}

for i in range(3):
    a = input().strip()
    cits[a] = len(a)
    
min_len = min(cits.values())
max_len = max(cits.values())

print(get_key(cits, min_len))
print(get_key(cits, max_len))