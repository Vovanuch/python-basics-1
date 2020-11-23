'''

Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Двоичной записью числа называется его запись в двоичной системе счисления.

Примечание 2:
﻿Данная задача очень просто может быть решена приведением строки к целому числу и проверке остатка от деления на три, но мы все же предлагаем вам решить ее, не используя приведение к числу.

Sample Input:

0
10010
00101
01001
Not a number
1 1
0 0

Sample Output:

0
10010
01001

'''

import re
import sys

patt = r'0*(1(00)*10*|10(00)*1(00)*(11)*0(00)*10*)*0*'
patt_digit01 = r'[01]'
repl = r''

for line in sys.stdin:
    line = line.strip()
    f = re.findall(patt_digit01, line)
    #print(f)
    if len(f) == len(line):
        #print('good binary.')
        #f1 = re.findall(patt, line)
        #print(f1)
        #if len(f1) > 0:
        d = 0
        len_line = len(line)
        #print(len_line)
        for i in range(len_line):
            #print('line[i]', line[i])
            #print('2**(len_line-i-1) = ', 2**(len_line-i-1))
            d += int(line[i])*(2**(len_line-i-1))
            #print(f'd = {d}')
        if (d % 3) == 0:
            print(line)
    
    if line == "!":
        break
