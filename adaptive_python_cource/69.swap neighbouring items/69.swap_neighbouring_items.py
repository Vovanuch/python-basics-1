'''


Swap the position of neighbouring items of the list (A[0] with A[1], A[2] with A[3] etc.). If there is odd number of elements in the list, the last element remains at its position.

Input data format

The first line of the input contains the number of elements in the array. The second line contains the elements of the array.

Sample Input:

5
1 2 3 4 5

Sample Output:

2 1 4 3 5

'''
def swap_cols(list_i):
    # calculate the count of columns to swap
    count = len(list_i) if (len(list_i)%2 == 0) else (len(list_i)-1)
    # swap cols
    for i in range(0, count, 2):
        list_i[i], list_i[i+1] = list_i[i+1], list_i[i]     
    
    return list_i

n = int(input().strip())
list_i = swap_cols(list(map(int, input().strip().split())))

print(*list_i)