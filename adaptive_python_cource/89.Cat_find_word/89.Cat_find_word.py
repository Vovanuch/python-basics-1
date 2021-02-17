'''


Given a sequence of lines.
Output all the lines, which contain "cat" as a word.

Note:                                                                                        Use the groups of symbols \b и \B to work with words.                                 

You can find the description of these groups in the documentation.

Sample Input:

cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:

cat
catapult and cat
"cat"
!cat?

'''
import sys
import re

p = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    f = re.findall(p, line)
    if len(f) > 0:
        print(line)

