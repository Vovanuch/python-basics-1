'''
Write a program that reads integers from the input one number per line.

For each of the entered numbers please check:
if the number is less than 10, then skip that number;
if the number is greater than 100, then stop reading numbers;
in any other cases bring the number back to the console in a separate line.

 Sample Input 1:

12
4
2
58
112

Sample Output 1:

12
58

Sample Input 2:

101

Sample Output 2:

Sample Input 3:

1
2
102

Sample Output 3: 

'''

while True:
    n = int(input().strip())
    if n < 10:
        continue
    elif 10 <= n <= 100:
        print(n)
    elif n > 100:
        break
    