'''

Простые числа

На вход программе подается два натуральных числа aaa и bbb (a< ba < ba< b). Напишите программу, которая находит все простые числа от aaa до bbb включительно.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести все простые числа от aaa до bbb включительно, каждое на отдельной строке.

Sample Input 1:

2
15

Sample Output 1:

2
3
5
7
11
13

Sample Input 2:

1
5

Sample Output 2:

2
3
5

'''

def count_delitels(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    return count

a = int(input().strip())
b = int(input().strip())
list_simple = [] 

for i in range(a, b+1):
    if count_delitels(i) == 2:
        list_simple.append(i)
        
print(*list_simple, sep = '\n')