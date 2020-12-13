'''


Given a sequence of natural numbers from the range [1, 2147483647]. 

Find whether you can represent these numbers as arithmetic progression. You can change the order of numbers in the sequence, if necessary.

You should write a program to solve this problem.

Input data

Input line contains a sequence of natural numbers. The length of the sequence can be from 1 to 100 000. The numbers are separated by spaces.

Output data

The output should contain either «Yes» in the case of positive reply or «No» otherwise.

Sample Input:

10 30 40 20

Sample Output:

Yes

'''

def is_arifm_prog(my_list):
    # length of list
    len_list = len(my_list)
    is_a_arifm_prog = True
    # if more than one elemetn
    if len_list > 1:
        # calculate dif in sorted list between 1st and 2nd element
        dif = my_list[1] - my_list[0]
        # for 2nd and others elements check, if it equal prev + dif. If not - quit.
        for i in range(1,len_list):
            if my_list[i] != my_list[i-1] + dif:
                is_a_arifm_prog = False
                break
    print('Yes') if (is_a_arifm_prog) else print('No')
    
    

list_n_base = list(map(int, input().strip().split()))
list_n = sorted(list_n_base)
is_arifm_prog(list_n)