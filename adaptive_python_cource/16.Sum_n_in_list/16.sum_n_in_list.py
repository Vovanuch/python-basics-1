'''



Write a program: input of this program has a single line with integers. The program must output the sum of these numbers.

Use the string method split.

Sample Input:

4 -1 9 3

Sample Output:

15


'''

list_n = input().strip().split()
list_n = [int(i) for i in list_n]
sum_n = sum(list_n)
print(sum_n)