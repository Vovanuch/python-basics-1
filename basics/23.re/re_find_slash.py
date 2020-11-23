'''

Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".

Sample Input:

\w denotes word character
No slashes here

Sample Output:

\w denotes word character

'''

import sys
import re

p = r'\\'

for line in sys.stdin:
    line = line.rstrip()
    f = re.findall(p, line)
    if len(f) > 0:
        print(line)
    if line == "!":
        break