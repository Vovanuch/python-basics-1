'''


The sum of digits of a three-digit number

Given a three-digit integer (i.e. an integer from 100 to 999). Find the sum of its digits.

Sample Input:

476

Sample Output:

17

'''

try:
    string = input().strip()
    sum = 0
    for i in string:
        sum += int(i)
    print(sum)
except:
    print('Wrong input')