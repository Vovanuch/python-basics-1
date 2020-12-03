'''


The last number

Given a natural number, not exceeding 10000. Output its last digit.

Sample Input:

753

Sample Output:

3

'''
s = input().strip()
print(s[-1])

# 2nd way, with integers:
# i = int(input().strip())
# print(i % 10)