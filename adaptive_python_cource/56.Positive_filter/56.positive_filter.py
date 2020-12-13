'''


Write the function filter_positive, which takes a list of numbers as input, and, not changing this list, returns the new list containing only the positive elements of it

You should not write input and output, only a function.

Sample Input:

-5 4 -8 12 2 -3 8

Sample Output:

-5 4 -8 12 2 -3 8
4 12 2 8

'''

def filter_positive(list_nums):
    my_list = []
    for i in list_nums:
        if i > 0:
            my_list.append(i)
    
    return my_list