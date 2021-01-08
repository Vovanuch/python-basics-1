''' fibonacci function 3 '''


def fib(x):
    if (x == 0) or (x ==1):
        #print(1, end = ' ')
        return 1
    else:
        #print(fib(x-1) + fib(x-2), end = ' ')
        return(fib(x-1) + fib(x-2))

print('Please, enter positive integer fo Fibo collection')
n = int(input())
res = fib(n)
print(res)
