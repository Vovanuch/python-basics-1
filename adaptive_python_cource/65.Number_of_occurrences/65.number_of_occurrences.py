'''


Given two strings s and t, consisting of lowercase letters of the Latin alphabet.

Find the number of occurrences of the line t in the line s.

Example:

s = "abababa"
t = "aba"

There are 3 occurrences of the line t in the line s:

abababa
abababa
abababa

Sample Input 1:

abababa
aba

Sample Output 1:

3

Sample Input 2:

abababa
abc

Sample Output 2:

0

Sample Input 3:

abc
abc

Sample Output 3:

1

Sample Input 4:

aaaaa
a

Sample Output 4:

5

'''

def count_occurance(s1, s2):
    count = 0
    for i in range(len(s1)):
        if str(s1[i:]).startswith(s2):  
            count += 1
    return count
        

s1 = input().strip()
s2 = input().strip()

count = count_occurance(s1, s2)

        

print(count)