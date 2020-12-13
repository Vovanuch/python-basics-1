'''


As input your program receives the three strings – s, a, b, consisting of lowercase letters of the Latin alphabet.
In a single operation you can exchange all the occurrences of string a in s to the string b.

For example, s = "abab", a = "ab", b = "ba", then after one operation the string s will become "baba", after two operations – "bbaa", and all subsequent operations will not change the string s.

You need to find out after what minimum number of operations the string s will not contain occurrences of the string a, or to find out that it will not happen.

Output a single number – the minimum number of operations, after which the string s will have no occurrences of the string a.

If after any number of operations the string s will still contain the occurrences of a, output Impossible.

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

def replase_sub(s, a, b, count):
    # replacing function with counting attempts
    res_s = s
    if a in s:
        res_s = s.replace(a, b)
        if res_s == s:
            return (res_s, -1)        
        count += 1        
    return (res_s, count)



s = input().strip()
list_s = list(s)
a = input().strip()
b = input().strip()

count = 0
while count > -1:
    res_s = replase_sub(s, a, b, count)
    #print(res_s[0], res_s[1])
    if (res_s[1] == -1) or (res_s[1] > 10000):
        print('Impossible')
        break
    elif res_s[1] == count:
        print(res_s[1])
        count = -2
        break
    s = res_s[0]
    count = res_s[1]
    

