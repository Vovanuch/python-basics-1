'''


Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

Sample Input:

I need to understand the human mind
humanity

Sample Output:

I need to understand the computer mind
computerity

'''

import sys
import re

p = r"human"
r = r"computer"

for line in sys.stdin:
    line = line.strip()
    line = re.sub(p, r, line)
    print(line)
    if line == "!":
        break