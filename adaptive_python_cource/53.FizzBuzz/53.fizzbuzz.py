'''


Fizz Buzz is a classic programming problem. Here is its slightly modified version.

Write a program that takes the input of two integers: the beginning and the end of the interval (both numbers belong to the interval).

The program should output the numbers from this interval, but if the number is divisible by 3, you should output Fizz instead of it, if the number is divisible by 5 - output Buzz, and if it is divisible both by 3 and by 5 - output FizzBuzz.

Output each number or the word on a separate line.

Sample Input:

8 16

Sample Output:

8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16

'''

lis = input().strip().split()
n, m = int(lis[0]), int(lis[1])

for i in range(n, m+1):
    if (i%3 == 0) and (i%5 != 0):
        print('Fizz')
    elif (i%3 != 0) and (i%5 == 0):
        print('Buzz')
    elif (i%3 == 0) and (i%5 == 0):
        print('FizzBuzz') 
    else:
        print(i)
    