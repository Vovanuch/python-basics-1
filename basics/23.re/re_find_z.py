'''

Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:

zabcz
zzxzz


'''

import sys
import re

p = r'z\w{3}z'

for line in sys.stdin:
    line = line.rstrip()
    f = re.findall(p, line)
    if len(f) > 0:
        print(line)
    if line == "!":
        break