'''


Next even number

Given a natural number N, not greater than 10000. Output the even number following this N.

Sample Input 1:

7

Sample Output 1:

8

Sample Input 2:

8

Sample Output 2:

10

'''
n = int(input().strip())
print(((n // 2) + 1) * 2)