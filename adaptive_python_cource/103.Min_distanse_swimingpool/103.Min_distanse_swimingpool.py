'''


Swimming pool

Ian was swimming in the pool having size of N×M feets and got tired. At this moment he realized that he is at a distance of X feets from one of the long ledge (not necessarily from the nearest one) and Y feets from one of the short ledges. What is the minimum distance (in feets) Ian needs to swim in order to reach the swimming pool ledge?

The program input contains numbers N, M, X, Y.

Sample Input:

23
52
8
43

Sample Output:

8

'''
n = int(input().strip())
m = int(input().strip())
x = int(input().strip())
y = int(input().strip())

print(min(x, y))