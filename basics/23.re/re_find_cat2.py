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

p = r'cat'

for line in sys.stdin:
    line = line.rstrip()
    f = re.findall(p, line)
    if len(f) > 1:
        print(line)
