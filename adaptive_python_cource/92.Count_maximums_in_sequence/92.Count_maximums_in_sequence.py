'''


The element of a sequence is called a local maximum, if it is strictly greater than the previous and the subsequent element of the sequence. The first and the last elements of the sequence are not the local maximum.

Given the sequence of natural numbers, ending with number 0. The number 0 itself is not included into the sequence and serves as a sign of its end.

Find the number of strict local maximums in this sequence.

Sample Input:

1
2
1
2
1
0

Sample Output:

2

'''
list_n = []
count_max = 0

while True:
    a = int(input().strip())
    if a == 0:
        break
    list_n.append(a)
    
m = max(list_n)
count_max = list_n.count(m)
print(count_max)