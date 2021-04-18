'''


Print the sum of all integers from a to b (a < b).

Sample Input:

8
24

Sample Output:

272

'''
def sum_in_range(n, m):
    s = sum(range(n, m+1))
    #for i in range(n, m+1):
    #    s += 
    return s


a, b = int(input().strip()), int(input().strip())
s = sum_in_range(a, b)
print(s)

    
