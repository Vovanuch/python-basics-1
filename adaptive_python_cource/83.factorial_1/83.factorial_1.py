'''


A user inputs a number M. You need to find out what is the smallest integer n such that n! > M.

Just in case: wiki on factorials.

Sample Input:

6188989133

Sample Output:

13

'''
import math

m = int(input().strip())
n = 1
while True:
    if math.factorial(n) > m:
        print(n)
        break
    else:
        n += 1
