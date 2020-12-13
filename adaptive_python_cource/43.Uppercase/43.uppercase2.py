'''


Input a single character and change its register. That is, if the lowercase letter has been entered – make it uppercase, and vice versa. Characters that are not Latin ones need to stay unchanged.

Sample Input:

b

Sample Output:

B

'''

s = input().strip()

if s.islower():
    print(s.upper())
elif s.isupper():
    print(s.lower())
else:
    print(s)