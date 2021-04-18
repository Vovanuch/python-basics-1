'''


In this problem, you need to implement the function, which shifts the contents of the array to the left for a specified number of positions (circular shift).

On input, the function takes the array, its size and the value of the shift. For example, if on input the function receives the array: a = [ 1, 2, 3, 4, 5 ]; and you need to circularly shift it 2 positions to the left, on the output we will get the numbers in the following order: 3, 4, 5, 1, 2.

Note that the value of the shift may be zero, and may be larger than the size of the array; please take into account all these cases.

Recommendation: Before you start coding the solution to this problem, consider the algorithm that you will use. In this problem, the effectiveness of this algorithm is not checked (in reasonable limits).

Sample Input 1:

10 2
21979 10841 -7714 -19302 -8293 -9557 -28558 -20525 10113 12835

Sample Output 1:

-7714 -19302 -8293 -9557 -28558 -20525 10113 12835 21979 10841

Sample Input 2:

2 4
22888 -22264

Sample Output 2:

22888 -22264

'''
#n, move = int(input().strip()), int(input().strip())
list_params = input().split()
n, move = int(list_params[0]), int(list_params[1])

list_n = [int(i) for i in input().split()]
list_n_2 = []

for i in range(n):
    list_n_2.append(list_n[(i + move) % n])
print(*list_n_2)