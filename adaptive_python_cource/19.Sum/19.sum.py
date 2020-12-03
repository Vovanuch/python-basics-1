'''


Find the sum of two numbers.

Sample Input:

3 8

Sample Output:

11

'''

try:
    lis = input().strip().split()
    lis = [int(i) for i in lis]
    print(sum(lis))
    
except:
    print('Incorrect input.')