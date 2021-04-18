'''


Given the number n, not greater than 100. Create the matrix of size n×n and fill it by the following rule. Numbers 0 should be stored on the primary diagonal. The two diagonals, adjacent to the primary one, should contain numbers 1. The next two diagonals - numbers 2, etc.

Sample Input:

5

Sample Output:

0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0

'''
n = int(input().strip())
list_n = [[-1] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        #if i == j:
        #    list_n[i][j] = 0 # i + j
        list_n[i][j] = i + j - 2 * i - 2 * j

for i in range(n):
    print(*list_n[i])