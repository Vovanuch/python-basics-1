'''
str funcs repr, join
'''
print(repr.__doc__)

nums = [i for i in range(1, 30, 3) if i%2 == 1]
print(nums)

lst_str_nums = map(str, nums)
print(lst_str_nums)
str_all_nums = ' '.join(lst_str_nums)
print(str_all_nums)