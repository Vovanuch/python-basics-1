'''


Given the list of numbers. Calculate how many pairs of elements are equal to each other. It is considered that any two elements, which are equal to each other, form one pair that you need to count.

Input data format

The first line contains the number of elements in the array. The second line contains the elements of the array.

Sample Input 1:

5
1 2 3 2 3

Sample Output 1:

2

Sample Input 2:

5
1 1 1 1 1

Sample Output 2:

10

'''

n = int(input().strip())
list_n = [int(i) for i in input().split()]
count = 0

for i in range(n):
    for j in range(i+1, n):
        if list_n[i] == list_n[j]:
            count += 1
            
print(count)