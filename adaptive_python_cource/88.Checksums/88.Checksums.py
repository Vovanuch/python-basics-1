'''


Checksums – the small values computed from the relatively large amounts of data, in order to ensure its consistency – i.e. to check that the data was not accidentally damaged, changed or partially lost.

Given an array, you need to calculate its checksum. This should be done as follows: each element (starting from the first one) is added to the current result (starting from 0); the resulting amount is multiplied by 113, then take the remainder by modulo 10000007 – this will be the new value of the result, and so on.

Input data contains the length of the array in the first line.
Elements of the array follow in the second line, space separated.

The output should contain a single number – the resulting checksum.

Sample Input:

6
1  3  2  4  5  6

Sample Output:

5242536

'''

n = int(input().strip())
res = 0
list_nums = [int(i) for i in input().strip().split()]
#print(list_nums)
for i in list_nums:
    res += i
    res *= 113
    res = res % 10000007

print(res)