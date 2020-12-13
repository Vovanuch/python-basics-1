'''


Transform the symbol into uppercase.

Input data

A single symbol.

Output data

If the entered symbol is a lowercase letter of the Latin alphabet, output the same uppercase letter. Otherwise, output the symbol that was entered.

Sample Input:

b

Sample Output:

B

'''
s = input().strip()
if (s >= 'a') and (s <= 'z'):
    print(s.upper())
else:
    print(s)