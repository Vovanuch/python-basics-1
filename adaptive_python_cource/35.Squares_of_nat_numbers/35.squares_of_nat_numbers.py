'''


Given integer N. Print all the squares of natural numbers, not exceeding N, in ascending order.

Sample Input:

50

Sample Output:

1
4
9
16
25
36
49


'''
try:
    n = int(input().strip())
    i = 1
    while i**2 <= n:
        print(i**2)
        i += 1
    
except:
    print('Incorrect input.')