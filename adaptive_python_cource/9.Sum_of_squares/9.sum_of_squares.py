'''


Write a program, which reads numbers from the input (by one in a line) until the sum of these numbers will not be equal to 0, and right after this outputs the sum of the squares of all read numbers.

It is guaranteed that at some moment the sum of the numbers will be equal to 0, and there is no need to continue reading after this.

In the example, we are reading numbers 1, -3, 5, -6, -10, 13; and at this moment, we notice that the sum of these numbers is equal to zero, therefore we output the sum of their squares, not paying attention to the remaining numbers.

Sample Input:

1
-3
5
-6
-10
13
4
-8

Sample Output:

340

'''

list_numbers = []
list_squares = []
sum_numbers = 0
sum_squares = 0

while True:
    num = int(input().strip())
    list_numbers.append(num)
    list_squares.append(num**2)
    sum_numbers += num
    if (sum_numbers == 0):
        sum_squares = sum(list_squares)
        print(sum_squares)
        break
