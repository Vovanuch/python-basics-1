'''


Given the list of integers, which may contain up to 100,000 numbers. Find how many different numbers are in this list.

Input data

Integer N - the number of elements in the list, and then the N numbers.

Sample Input:

5
1 2 3 2 1

Sample Output:

3

'''
try:
    n = int(input().strip())
    list_s = input().strip().split()
    set_s = set(list_s)
    print(len(set_s))
except:
    print('Incorrect input.')