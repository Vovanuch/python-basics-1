'''


Write a program with the function fib(n), which returns the n-th Fibonacci number by the given non-negative integer n. You can't use loops in this problem – use the recursion.

First and second Fibonacci numbers are equal to 1, and each next one is equal to the sum of the two previous numbers.

Your program should read the n, call the fib(n) function and print the answer.

Sample Input:

1

Sample Output:

1

'''
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 .....
def fib(n):
    if (n == 0):
        return 0    
    elif (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
        

n = int(input().strip())
print(fib(n))