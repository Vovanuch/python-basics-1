'''


The average value

Given the sequence of integers, ending with number 0. Find the average value of all elements in this sequence.

The number 0 itself is not included into the sequence and serves just as a sign of cessation.

Sample Input:

1
7
9
0

Sample Output:

5.66666666667

'''
count = 0
list_int = []
while True:
    n = int(input().strip())
    if n != 0:
        list_int.append(n)
    else:
        break
    
aver = sum(list_int) / len(list_int)
print(aver)