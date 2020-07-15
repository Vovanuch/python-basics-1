''' exeptions 4 '''

my_var = input('Введите значение: ')

try:
    int(my_var)
    print('This var can be integer!')
except Exception as e:
    print('Sorry, this var isnt integer.')
else:
    #print(str(my_var))
    my_doubled_var = int(my_var) * 2
    print('Doubled var is: ', my_doubled_var)
finally:
    print('Never give up!')
    
