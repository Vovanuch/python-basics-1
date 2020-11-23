'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample

Input:

attraction
buzzzz

Sample Output:

atraction
buz
'''

import sys
import re
patt = r'(\w+)\1'
repl = r'\1'

def sub_retry(patt, repl, line):
    len1 = len(line)
    line = re.sub(patt, repl, line)
    len2 = len(line)
    if len1 == len2:
        return line
    else:
        return sub_retry(patt, repl, line)

for line in sys.stdin:
    line = line.strip()
    #line = re.sub(patt, repl, line)
    line = sub_retry(patt, repl, line)
    print(line)
    if line == "!":
        break