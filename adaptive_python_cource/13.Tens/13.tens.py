'''
The number of tens

Given a non-negative integer N (0 ≤ N ≤ 1000000), find the number of tens in it (i.e. next to last digit of the number). If there is no next to last digit, you can consider that the number of tens equals to zero.
'''

try:
    a = int(input().strip())
    b = a % 100
    c = b // 10
    print(c)
except:
    print('Your data is uncorrect')