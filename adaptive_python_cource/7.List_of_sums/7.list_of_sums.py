'''
Write a program the input of which is the list of numbers in one line. For each elements of this list, the program should output the sum of its two neighbouring numbers. For list item that is first or last, an element from the opposite end of the list is considered in place of a missing neighbour. For example, if the input list is "1 3 5 6 10", the expected output list is "13 6 9 15 7" (without quotation marks).

If only one number serves as input, the output shall display the same one number.

The output must contain one line with the numbers from the new list, separated by space.



Sample Input 1:

1 3 5 6 10

Sample Output 1:

13 6 9 15 7

Sample Input 2:

10

Sample Output 2:

10


'''
def to_int(my_list):
    for i in my_list:
        i = int(i)
    return my_list

def get_list_sums(my_list):
    list_sums = []
    le = len(my_list)
    if le <= 1:
        list_sums = my_list
        return list_sums
    
    for i in range(le):
        i_1 = my_list[(i-1)%le]
        #print('left s', i_1)
        i_2 = my_list[(i+1)%le]
        #print('right s', i_2)
        sum_i = int(i_1) + int(i_2)
        list_sums.append(sum_i)
    
    return list_sums


s = input().strip()
list_int = s.split()
list_int = to_int(list_int)
list_sums = get_list_sums(list_int)


    
#print(list_int)
print(*list_sums)