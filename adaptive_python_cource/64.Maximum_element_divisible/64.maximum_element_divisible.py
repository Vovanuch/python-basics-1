'''


Given a sequence of natural numbers, not exceeding 30000. Find the its maximum element divisible by 4. As input, the program gets the number of elements in the sequence, and then the elements themselves. In the sequence, there is always an element divisible by 4. The number of elements does not exceed 1000. The program should print the single number – the maximum element of the sequence divisible by 4.

Sample Input:

12
16
18
62
36
19
12
66
68
32
14
89
8

Sample Output:

68

'''

def get_int_list_from_input(col):
    my_list = []
    for i in range(col):
        my_list.append(int(input().strip()))
    return my_list

def get_max_divided_item(my_list, div):
    my_list = sorted(my_list, reverse=True)
    max_item = -1000
    for i in my_list:
        if i % div == 0:
            max_item = i
            break
    return max_item


col = int(input().strip())
list_int = get_int_list_from_input(col)
res = get_max_divided_item(list_int, 4)
print(res)