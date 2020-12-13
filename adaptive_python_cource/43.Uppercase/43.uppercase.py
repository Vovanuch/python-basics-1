'''


Input a single character and change its register. That is, if the lowercase letter has been entered – make it uppercase, and vice versa. Characters that are not Latin ones need to stay unchanged.

Sample Input:

b

Sample Output:

B

'''

s = input().strip()

if s >= 'a' and s <= 'z':
    print(s.upper())
elif s >= 'A' and s <= 'Z':
    print(s.lower())
else:
    print(s)