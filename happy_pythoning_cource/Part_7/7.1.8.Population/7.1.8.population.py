'''

Популяция

На вход программе подается три натуральных числа m, p, nm, \, p, \, nm,p,n:

    m:m:m: стартовое количество организмов;
    p:p:p: среднесуточное увеличение в %;
    n:n:n: количество дней для размножения.

Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, начиная с 111 и заканчивая nnn-м днем.

Формат входных данных
На вход программе подается три натуральных числа.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

10
50
6

Sample Output 1:

1 10.0
2 15.0
3 22.5
4 33.75
5 50.625
6 75.9375

Sample Input 2:

100
25
1

Sample Output 2:

1 100

Sample Input 3:

120
25
4

Sample Output 3:

1 120.0
2 150.0
3 187.5
4 234.375

'''

m = int(input().strip())
p = int(input().strip())
n = int(input().strip())

for i in range(1, n+1):
    print(f'{i} {m}')
    m *= (1 + (p/100))
    