'''


Upon learning that DNA is not a random string, freshmen of the Bioinformatics Institute from the informatics group suggested using a compression algorithm that compresses repeated characters in a string.

Encoding is performed as follows:
s = 'aaaabbсaa' is converted into 'a4b2с1a2', that is, the groups of the same characters of the input string are replaced by the symbol and the number of its repetitions in this string.

Write a program, which reads the string, encodes it by this algorithm and outputs the encoded sequence. Encoding must be case sensitive.

Sample Input 1:

aaaabbcaa

Sample Output 1:

a4b2c1a2

Sample Input 2:

abc

Sample Output 2:

a1b1c1

'''

def find_kol_alpha(my_str, alpha, pos_start):
    c_alpha = 0
    for i in range(pos_start, len(my_str)):
        if my_str[i] == my_str[pos_start]:
            c_alpha += 1
        else:
            return c_alpha
            break
    return c_alpha
'''
def get_list_symbols(my_list):
    new_list = []
    ex_counter = 0
    for i in my_list:
        ex_counter += 1
        if i not in new_list:
            new_list.append(i)
        elif i != new_list[len(new_list)-1]:
            new_list.append(i)
    
    return new_list
'''

def get_dict_symbols(my_list):
    new_dict = dict()
    new_list = []
    ex_counter = 0
    for i in my_list:
        ex_counter += 1
        if i not in new_list:
            new_list.append(i)
            new_dict[ex_counter] = i
        elif i != new_list[len(new_list)-1]:
            new_list.append(i)
            new_dict[ex_counter] = i
    
    return new_dict


try:
    text = input().strip()
    
    dict_symbols = get_dict_symbols(text)
    
    for k,v in dict_symbols.items():
        count_a = find_kol_alpha(text, v, k-1)
        print(v, count_a, sep='',end='')
   
except Exception:
    print('Incorrect input.', Exception)