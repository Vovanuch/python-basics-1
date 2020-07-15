'''

В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

Sample Input 1:

2016 4 20
14

Sample Output 1:

2016 5 4

Sample Input 2:

2016 2 20
9

Sample Output 2:

2016 2 29

Sample Input 3:

2015 12 31
1

Sample Output 3:

2016 1 1
'''
import datetime

lst_date = []
lst_date_2 = []
int_delta = 0
str_result = ''

lst_date = input().strip().split()
int_delta = int(input())

#for s in lst_date:
#    s = int(s)

#print(*lst_date)
#print(int_delta)

dt_date1 = datetime.date(int(lst_date[0]), int(lst_date[1]), int(lst_date[2]))
dt_date2 = dt_date1 + datetime.timedelta(int_delta)

#print(dt_date2)

str_date2 = str(dt_date2)
#print(str_date2)

lst_date_2 = str_date2.split('-')
#print(lst_date_2)

for s in lst_date_2:
    str_result += str(int(s))
    str_result += ' '

str_result = str_result.strip()
print(str_result)
