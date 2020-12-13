'''


Input, separated by spaces: the number of rows of the matrix, the number of columns of the matrix, then go the elements of the two-dimensional matrix itself, row by row.

Output: the result of the transposition of the matrix (row by row).

Sample Input:

2 3 1 2 3 4 5 6

Sample Output:

1 4 2 5 3 6

'''


def transponir_a(my_list, n, m):
    res_s = ''
    new_list = [[0] * n for i in range(m)]
    for row in range(len(my_list)):
        for col in range(len(my_list[row])):
            new_list[col][row] = my_list[row][col]
            
    for r in new_list:
        for c in r:
            res_s += str(c) + ' '
    
    return res_s

def get_matrix(my_list, n, m):
    matrix = []
    for i in range(0, n):
        matrix.append(list())
        for j in range(0, m):
            matrix[i].append(my_list[2+j+i*m])
    return matrix



list_s = input().strip().split()
list_i = [int(i) for i in list_s]

n = list_i[0]
m = list_i[1]

matrix = get_matrix(list_i, n, m)
res_s = transponir_a(matrix, n, m).strip()
print(res_s)

