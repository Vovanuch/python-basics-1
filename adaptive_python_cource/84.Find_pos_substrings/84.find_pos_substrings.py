'''


Write a program that finds all occurrences of the given substring in the string.

Input format:
The first line of input contains the original string, the second line contains the substring, the positions of which you should find. The lines consist of Latin characters only.

Output format:
A single line with the indices (indexing starts with zero) of the occurrences of the given substring in the string, separated by a space, or number -1 when the substring is absent.

Sample Input 1:

abacabadaba
aba

Sample Output 1:

0 4 8

Sample Input 2:

aaaa
aa

Sample Output 2:

0 1 2

Sample Input 3:

abc
d

Sample Output 3:

-1

'''
text = input()
sub = input()
pos = -1

for i in range(len(text)+1):
    if text[i:].startswith(sub):
        pos = i
        print(pos, end=' ')

if pos == -1:
    print(pos)