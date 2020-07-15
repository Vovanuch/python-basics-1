''' Тестовый файл для отработки'''

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

y = 2020
m = 7
d = 10

x = datetime.date(y, m, d)
print(x)

#datetime.now()
print( datetime.date(2012, 12, 14) )



dat = datetime.date(2012, 12, 14)
 
print('Year:', dat.year) # 2012
print('Day:',dat.day)  # 14
print('Month:',dat.month) # 12

dat2 = dat + datetime.timedelta(20)

print('dat2: ', dat2) 
