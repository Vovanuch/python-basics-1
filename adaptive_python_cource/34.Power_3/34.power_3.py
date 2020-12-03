'''


Given a real positive number a and an integer number n.

Find an a^n an.  You need to write the whole program with a recursive function power(a, n). 

Sample Input 1:

2
1

Sample Output 1:

2

Sample Input 2:

2
2

Sample Output 2:

4

'''

def power(a, n):
    return a**n

a = float(input().strip())
n = int(input().strip())
print(power(a, n))