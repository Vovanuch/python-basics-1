''' fibonacci function 2'''

def fibo(n=0):
    if n < 0:
        print('Please, enter correct value')
        return None 
    elif n == 0:
        return [0]
    elif 0 < n < 2:
        return [0, 1, 1]
    else:
        lst = [0, 1]
        while (lst[-1] + lst[-2]) <= n:
            lst.append(lst[-1] + lst[-2])
        return lst
            
print('Please, enter positive integer fo Fibo collection')
n = int(input())
result = fibo(n)
print(*result)
