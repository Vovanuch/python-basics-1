'''


Given the sequence of numbers, ending with number 0. Find the sum of all these numbers without using a loop.

Sample Input:

1
7
9
0

Sample Output:

17

'''

my_list = []
while True:
    n = int(input().strip())
    if n != 0:
        my_list.append(n)
    else:
        break
s = sum(my_list)
print(s)