'''


Find whether the given symbol is a digit.

Output "yes", is the symbol is a digit and "no" otherwise. Please note that you should output words in a lowercase.

Sample Input 1:

1

Sample Output 1:

yes

Sample Input 2:

a

Sample Output 2:

no

'''

s = input()
if s.isdigit():
    print('yes')
else:
    print('no')