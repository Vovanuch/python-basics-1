'''


Fractional part 2

Given a positive real number X. Output its first digit after the decimal point.

Sample Input:

1.79

Sample Output:

7

'''
def find_point(s):
    if '.' not in s:
        return(0)
    
    for i in range(len(s)-1):
        if (s[i] == '.'):
            return(int(s[i+1]))
            break

    
try:
    s = input().strip()
    print(find_point(s))

except:
    print('Incorrect input.')