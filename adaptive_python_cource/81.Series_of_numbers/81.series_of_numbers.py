'''
Given the series of numbers: 1, -0.5, 0.25, -0.125, ... . Try to understand how it works.
On the input, the program has integer n n n, and the output should be a real number corresponding to the sum of first n n n elements of the series.


Sample Input:

5

Sample Output:

0.6875

'''

n = int(input().strip())
list_nums = [1]

for i in range(1, n):
    list_nums.append((list_nums[i-1] / 2) * (-1))
    
print(sum(list_nums))