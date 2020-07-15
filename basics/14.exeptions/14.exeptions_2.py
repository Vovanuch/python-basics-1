''' exeptions 2 '''
try:
    my_list = [1, 2, 'list', 4]
    my_list.sort()
    print(my_list) #
except TypeError:
    print('Sorry, type error!')

print('I can sort!')
