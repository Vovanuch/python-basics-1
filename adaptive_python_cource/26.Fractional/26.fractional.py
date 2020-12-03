'''


Fractional part 1

Given a positive real number X. Output its fractional part.

Sample Input:

17.9

Sample Output:

0.9


'''

def find_real(s):
    if '.' not in s:
        return(0)
    
    for i in range(len(s)-1):
        if (s[i] == '.'):
            return('0.' + s[(i+1):])
            break

    
try:
    s = input().strip()
    print(find_real(s))

except:
    print('Incorrect input.')