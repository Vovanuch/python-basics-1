'''


Difference of times

Given the values of the two moments in time in the same day: hours, minutes and seconds for each of the time moments. It is known that the second moment in time happened not earlier than the first one. Find how many seconds passed between these two moments of time.

Input data format

The program gets the input of the three integers: hours, minutes, seconds, defining the first moment of time and three integers that define the second moment time.

Output data format

Output the number of seconds between these two moments of time.

Sample Input 1:

1
1
1
2
2
2

Sample Output 1:

3661

Sample Input 2:

1
2
30
1
3
20

Sample Output 2:

50

'''
try:
    p1, p2, d = dict(), dict(), dict()
    p1['h'] = int(input().strip())
    p1['m'] = int(input().strip())
    p1['s'] = int(input().strip())
    
    p2['h'] = int(input().strip())
    p2['m'] = int(input().strip())
    p2['s'] = int(input().strip())
    
    d['h'] = p2['h'] - p1['h']
    d['m'] = p2['m'] - p1['m']
    d['s'] = p2['s'] - p1['s']
    
    dif = d['h']*3600 + d['m']*60 + d['s']
    print(dif)

except:
    print('Incorrect input')