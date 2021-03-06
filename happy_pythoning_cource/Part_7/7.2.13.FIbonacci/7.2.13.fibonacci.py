'''

Последовательность Фибоначчи 🌶️

Напишите программу, которая считывает натуральное число nnn и выводит первые nnn чисел последовательности Фибоначчи.

Формат входных данных
На вход программе подается одно число n  (n≤100)n\,  (n \le 100)n (n≤100) – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Фибоначчи, отделенные символом пробела.

Примечание. Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих: 1,  1,  2,  3,  5,  8,  13,   21,  34,  55,  89,…1,  \, 1, \,  2, \,  3, \,  5, \,  8, \,  13, \,  21, \,  34, \,  55, \,  89, \ldots1, 1, 2, 3, 5, 8, 13,  21, 34, 55, 89,…

Sample Input 1:

1

Sample Output 1:

1

Sample Input 2:

5

Sample Output 2:

1 1 2 3 5

Sample Input 3:

22

Sample Output 3:

1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711

'''

def fib(n):
    list_fib = []
    if n == 1:
        list_fib.append(1)
    elif n == 2:
        list_fib = fib(n-1)
        list_fib.append(1)
        
    else:
        list_fib = fib(n-1)
        list_fib.append(list_fib[-2] + list_fib[-1])
        
    
    return list_fib
    
n = int(input().strip())
list_fibonacci = fib(n)
print(*list_fibonacci)