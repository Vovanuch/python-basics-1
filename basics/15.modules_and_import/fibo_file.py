''' fibonacci funtion'''

def fib(x):
    #if x.is_integer:
        #print(f'{x} is integer!')
    try:
        x = int(x)
        if x == 0 or x == 1:
            return 1
        elif x >= 2:
            return fib(x - 1) + fib (x - 2)
        else:
            print('Bad value!')
    except Exception as e:
        print(f'{x} is not a correct value for Fibonacci function.')
            
#x = input('Please, enter number for Fibonacci function: ')
#print(fib(x))

#fib('a')
