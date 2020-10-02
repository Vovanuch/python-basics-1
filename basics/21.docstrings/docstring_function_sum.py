'''
docstring test2. Functions.
'''

def sum_2(a=0, b=0):
    '''
    This is summ function, that converts to int two params
    '''
    try:
        return int(a) + int(b)
    except:
        print("Can't convert params to int. Please, check it.")
    finally:
        print('Welcome back!')

my_a, my_b = input('Please, enter two params for sum, separate it with spaces (1 2): ').split()
print(f'The summ is {sum_2(my_a, my_b)}')
print(sum_2.__doc__)