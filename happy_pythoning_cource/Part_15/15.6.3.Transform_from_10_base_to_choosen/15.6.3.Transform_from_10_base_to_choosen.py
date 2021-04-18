'''
Transform number from 10-base  to given base number
'''


def transform_to_base(my_number, my_base):
    list_osts = []
    dict_alp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    dict_nums = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    while my_number >= my_base:
        ost = my_number % my_base
        list_osts.append(dict_nums[ost])
        my_number = my_number // my_base
            
    list_osts.append(dict_nums[my_number])        
    
    return list_osts


def list_to_str(my_list):
    s = ''
    for i in my_list:
        s += str(i)
    
    return s

print('Введите число в десятичной системе счисления. ')
n = int(input().strip())
print('Введите базу системы счисления, в которую нужно перевести. ')
base = int(input().strip())

res = []
res = transform_to_base(n, base)
res_s = [str(i) for i in res[::-1]] 
res_s = list_to_str(res_s)
print(f'Это число в {base}-ной системе равно {res_s}')
