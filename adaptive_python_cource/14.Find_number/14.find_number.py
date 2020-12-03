'''


Given positive integer N N N. Find the number of positive integers less than N N N such that their sum of digits (in decimal notation) is equal to the sum of digits in the number N N N. Output the number of such integers.

Sample Input:

123

Sample Output:

9


'''

def sum_digit(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

try:
    n = int(input().strip())
    
    sum_digit_n = sum_digit(n)
    
    count = 0
    for i in range(n):
        s = sum_digit(i)
        if (sum_digit_n == s):
            count += 1
            
    print(count)
    
except:
    print('Uncorrect input.')