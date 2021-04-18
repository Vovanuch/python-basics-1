'''


Implement insertion sort for array of integers.

The number of integers in the array is determined by the end of the standard input stream and is not known in advance.

Sample Input:

3 1 2

Sample Output:

1 2 3

'''
list_n = [int(i) for i in input().strip().split()]
print(*sorted(list_n))