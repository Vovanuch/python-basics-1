'''


Given the four real numbers: x1, y1, x2, y2. Write the function distance(x1, y1, x2, y2), calculating the distance between the point (x1. y1) and point (x2, y2).

Read the four real numbers and output the result of this function's call.

Sample Input:

0
0
1
1

Sample Output:

1.41421

'''

def distance(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    c = (a**2 + b**2)**0.5
    return c

x1, y1, x2, y2 = float(input().strip()), float(input().strip()), float(input().strip()), float(input().strip())
c = distance(x1, y1, x2, y2)
print(c)
