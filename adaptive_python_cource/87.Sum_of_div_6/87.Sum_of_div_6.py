'''


Given the sequence of natural numbers. Find the sum of numbers, divisible by 6. The input is number of elements in the sequence, and then the elements themselves. In this sequence, there is always a number, divisible by 6.

Sample Input:

8
35
6
44
36
64
12
89
81

Sample Output:

54

'''

n = int(input().strip())
list_nums = [int(input().strip()) for _ in range(n)]
s = 0

for i in list_nums:
    if i % 6 == 0:
        s += i
        
print(s)