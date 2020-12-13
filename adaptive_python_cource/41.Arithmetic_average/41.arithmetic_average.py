'''


Arithmetic average

Write a program that reads two numbers a a a and b b b from the keyboard, calculates and outputs to the console the arithmetic average of all numbers from the interval [a;b] [a; b] [a;b], which are divided by 3 3 3.

In the example below the arithmetic average is calculated for the numbers on the interval [−5;12] [-5; 12] [−5;12]. Total numbers divided by 3 3 3 on this interval 6 6 6: −3,0,3,6,9,12 -3, 0, 3, 6, 9, 12 −3,0,3,6,9,12. Their arithmetic average equals to 4.5 4.5 4.5 

The program input contains intervals, which always contain at least one number, which is divided by 3 3 3.

Sample Input:

-5
12

Sample Output:

4.5

'''

try:
    a, b = int(input().strip()), int(input().strip())
    list_3 = []
    for i in range(a, b+1):
        if i%3 == 0:
            list_3.append(i)
            
    arithmetic_average = sum(list_3)/len(list_3)
    print(arithmetic_average)
    
except:
    print('Incorrect input.')
