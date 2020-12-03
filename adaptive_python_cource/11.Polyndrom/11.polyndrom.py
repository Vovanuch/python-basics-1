'''


Given a string. Find whether it is a palindrome, i.e. it reads the same both left-to-right and right-to-left. Output “yes” if the string is a palindrome and “no” otherwise.

Sample Input:

kayak

Sample Output:

yes

'''
my_str = input().strip()
if my_str == my_str[::-1]:
    print('yes')
else:
    print('no')