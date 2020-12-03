'''
Write a program that takes a list of integers as input, and outputs the values that are repeated in it more than once.

You may need the list method sort to solve this problem.

Input format:
One line with integers, separated by a space.

Output format:
A line with integers, separated by a space. The numbers must not be repeated, the output order can be arbitrary.
'''

list_str = input().strip().split()
#print(list_str)
#list_n = []
list_n = [int(i) for i in list_str]

list_n_not_uniq = []

for i in list_n:
    if list_n.count(i) != 1:
        list_n_not_uniq.append(i)

list_final = list(set(list_n_not_uniq)) 

print(*list_final)