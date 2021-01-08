''' fibonacci function '''

def fibo(n=0):
    x = 0
    lst = []
    if n < 0:
        print('Please, enter correct value')
        return None
#'''
    elif n == 0:
        lst = [0]
        return lst

    elif n == 1:
        lst = [0, 1, 1]
        return lst
#'''        
    else:
        lst = [0, 1]
        while (lst[-1] + lst[-2]) <= n:
            lst.append(lst[-1] + lst[-2])
        return lst
            
print('Please, enter positive integer fo Fibo collection')
n = int(input())
result = fibo(n)
print(*result)
        
