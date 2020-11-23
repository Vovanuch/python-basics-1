'''

Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line


Sample Input:

catcat
cat and cat
catac
cat
ccaatt

Sample Output:

catcat
cat and cat

'''

import sys
import re

def finditall(p='', s=''):
    r = re.findall(p, s)
    print(f'We find {len(r)} ({r}) items in "{s}" string, that match to "{p}" template.')



lines = []
s = 'cat'
for i in range(5):
    lines.append(s * i)

print('Our array of lines is: ', *lines)

p = r'cat'

for l in lines:
    print(f'Current line is {l}')
    finditall(p, l)
    f = re.findall(p, l)
    if len(f) > 1:
        print(f'So, {len(f)} more than 2, and we print the current line: ',l)
        


#for line in sys.stdin:
#    line = line.rstrip()
    


