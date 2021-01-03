'''

Обратный порядок 1

Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести цифры введенного числа в столбик в обратном порядке.

Sample Input 1:

12345

Sample Output 1:

5
4
3
2
1

Sample Input 2:

55690454

Sample Output 2:

4
5
4
0
9
6
5
5

Sample Input 3:

9673210458

Sample Output 3:

8
5
4
0
1
2
3
7
6
9

'''

# One row decision:
#print(*list(input().strip()[::-1]), sep='\n')

n = int(input().strip())

while n > 0:
    print(n%10)
    n = n // 10