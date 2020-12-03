'''


Given number N. Print all integer powers of two, not exceeding N, in ascending order.

Sample Input:

50

Sample Output:

1
2
4
8
16
32

'''
try:
    n = int(input().strip())
    p = 0
    while True:
        if (2**p) <= n:
            print(2**p)
            p += 1
        else:
            break
    
except:
    print('Incorrect input.')