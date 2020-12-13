'''


Given a two-dimensional array (matrix) and the two numbers: i and j. Swap the columns with indices i and j within the matrix.

Input contains matrix dimensions n and m, not exceeding 100, then the elements of the matrix, then the indices i and j.

Sample Input:

3 4
11 12 13 14
21 22 23 24
31 32 33 34
0 1

Sample Output:

12 11 13 14
22 21 23 24
32 31 33 34

'''

def generate_zero_matrix(n, m):
    my_matrix = [[0]*m for i in range(n)]
    return my_matrix

def fill_matrix_from_input(my_matrix, n):
    for i in range(n):
        my_matrix[i] = input().strip().split()
    return my_matrix


def replace_column_matrix(my_matrix, i, j):
    for r in my_matrix:
        r[i], r[j] = r[j], r[i]
    return my_matrix
    
def print_matrix(my_matrix):
    for r in matrix:
        for c in r:
            print(c, end=' ')
        print()
        

n, m = input().strip().split()
n = int(n)
m = int(m)

matrix = generate_zero_matrix(n, m)  #[[0]*m for i in range(n)]

matrix = fill_matrix_from_input(matrix, n)

i, j = input().strip().split()
i = int(i)
j = int(j)

matrix = replace_column_matrix(matrix, i, j)

print_matrix(matrix)
