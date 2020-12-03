'''


Write a program that inputs the distance between the two cities in miles and the travel time by bus in hours, and outputs the average speed of the bus.

Note: there is NO need to give any explanations during input and output.

Sample Input:

100
2

Sample Output:

50.0

'''

try:
    #lis = input().strip().split()
    #lis = [int(i) for i in lis]
    dis = float(input().strip())
    hours = float(input().strip())
    speed = dis / hours
    print(speed)
    
except:
    print('Incorrect input.')