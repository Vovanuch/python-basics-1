'''


Write a function that takes a positive three-digit number as input and returns the sum of its digits.

The function should have a name digit_sum and take an argument n.

Sample Input:

943

Sample Output:

16

'''

def digit_sum(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    
    return sum

n = input().strip()
print(digit_sum(n))