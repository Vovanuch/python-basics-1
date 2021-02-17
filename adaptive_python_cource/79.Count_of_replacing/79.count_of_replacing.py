'''


Given three strings – s, a, b, which consist of lowercase Latin letters.
In one operation you may replace all occurrences of the substring a in the string s to the string b.

For example, s = "abab", a = "ab", b = "ba", then after performing one operation the string s goes to the string "baba", after performing two operations – to the string "bbaa", and all further operation will not alter the string s.

You need to find out after how many operations there will be no occurrences of string a in the string s, or to find out that this will not happen.

Output a single number – the number of operations after which there will be no occurrences of the string a in the string s. 

If after performing any number of operation there still will be occurrences of the string a in the string s, output Impossible.

Sample Input 1:

ababa
a
b

Sample Output 1:

1

Sample Input 2:

ababa
b
a

Sample Output 2:

1

Sample Input 3:

ababa
c
c

Sample Output 3:

0

Sample Input 4:

ababac
c
c

Sample Output 4:

Impossible

'''
def str_repl(text, was, will):
    res = text.replace(was, will)
    return res


s, a, b = input().strip(), input().strip(), input().strip()
#x = 'asd'
#x.replace
count = 0
counted = True

while True:
    if (a not in b):
        r = str_repl(s, a, b)
        #print(r)
        if r != s:
            count += 1
            s = r
        else:
            break
    else:
        if a in s:
            print('Impossible')
            counted = False
            break
        else:
            break

if counted:
    print(count)
