'''


Write a program that reads an integer from the input (a non-negative one), and outputs this number to the console together with a correctly changed word "contig", for example: 1 contig, 5 contigs.

Sample Input:

5

Sample Output:

5 contigs

'''
n = int(input().strip())
s = 'contig'
if n == 1:
    print(n, s)
else:
    print(n, s+'s')