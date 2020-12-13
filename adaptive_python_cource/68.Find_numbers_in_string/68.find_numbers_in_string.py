'''


Input – one line of random text. The text contains words and integer numbers. Your program should calculate and output the sum of all integers that appear in the text.

Sample Input 1:

3 5 2 2 10 quick over 9 fox brown dog

Sample Output 1:

31

Sample Input 2:

dog 6 5 3 lazy quick The

Sample Output 2:

14

Sample Input 3:

The the 4 lazy 4 The 4 jumps over jumps 3

Sample Output 3:

15

'''
def get_list_int(my_list):
    new_list = []
    for elem in my_list:
        try:
            new_list.append(int(elem))
        except:
            pass
    return new_list


list_s = input().strip().split()
list_i = get_list_int(list_s)
summ = sum(list_i)
print(summ)