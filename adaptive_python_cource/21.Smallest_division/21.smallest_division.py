'''


The smallest natural divisor

Given an integer, not less than 2. Find its smallest natural divisor, different from 1.

Sample Input:

15

Sample Output:

3

'''
try:
    #lis = input().strip().split()
    #lis = [int(i) for i in lis]
    n = int(input().strip())
    for i in range(2, n+1):
        if (n%i) == 0:
            print(i)
            break
    
    
except:
    print('Incorrect input.')