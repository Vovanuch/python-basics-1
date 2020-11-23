'''
regexp
'''

import re

# . = любой 1 сифвол
# ^ = НЕ
# * - либое количество символов
# \d = [0-9], цифры от 0 до 9
# \D = [^0-9], НЕ цифры от 0 до 9
# \s = [\t\n\r\f\v] - пробельные символы
# \S = [^\t\n\r\f\v] - НЕ пробельные символы
# \w = [a-zA-Z0-9_] - буквы + цифры + пробел

pattern = '\d'
a = [1, 2, 3, '4', '5', '6']
# res = re.findall(pattern, a) - ошибка, т.к. findall принимает только строку. Список - не хочет.
res = re.findall(pattern, str(a))
print(res)
res2 = []
for i in a:
    res2.append(re.findall(pattern, str(i)))
print(res2)
    
    
print()
print()
temp_str = r'ajmnx cvbSsk\nlgfdhj83267-gfRdn572*0!DgdnX'
p1 = '\w'
p2 = '\d'
p3 = '\s'
p4 = '[a-z]'
p5 = '[A-Z]'
p6 = '[^a-z0-9]' # исключили все маленькие буквы и цифры

res1 = re.findall(p1, temp_str)
res2 = re.findall(p2, temp_str)
res3 = re.findall(p3, temp_str)
res4 = re.findall(p4, temp_str)
res5 = re.findall(p5, temp_str)
res6 = re.findall(p6, temp_str)

print(f'String s is: "{temp_str}"')
print('res1, w: ', res1)
print('res2, d: ', res2)
print('res3, s: ', res3)
print('res4, s: ', res4)
print('res5, s: ', res5)
print('res6, s: ', res6)
