'''


Interval

Given an integer as input. Output True if its value is within the interval (−15,12]∪(14,17)∪[19,+∞) (-15, 12] \cup (14, 17) \cup [19, +\infty) (−15,12]∪(14,17)∪[19,+∞), and False otherwise (case sensitive).

Please note the different brackets, which are used to specify intervals. The problem uses semi-open and open intervals. You can read more about it on the Wikipedia.

Sample Input 1:

20

Sample Output 1:

True

Sample Input 2:

-20

Sample Output 2:

False

'''
n = int(input().strip())

if (-15 < n <= 12) or (14 < n < 17) or (19 <= n):
    print(True)
else:
    print(False)