'''
this is for finding differences and commons in strings
'''

str1 = 'abcdefg'
str2 = 'acefgtj'

diff = []
comm = []

def function_diff_symbols_in_strs(s1, s2):
    diff = []
    for i in s1:
        if i not in s2:
            diff.append(i)
            
    for j in s2:
        if j not in s1:
            diff.append(j)
    return diff


def function_common_symbols_in_strs(s1, s2):
    common = []
    for i in s1:
        if i in s2 and i not in common:
            common.append(i)
            
    for j in s2:
        if j in s1 and j not in common:
            common.append(j)
    return common



diff = function_diff_symbols_in_strs(str1, str2)
comm = function_common_symbols_in_strs(str1, str2)

print(f'diffrence between strings are:', *diff)
print(f'Common symbols in strings are:', *comm)
#print(diff)        
#print(*diff)