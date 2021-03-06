'''

Знакочередующаяся сумма

На вход программе подается натуральное число nnn. Напишите программу вычисления знакочередующей суммы 1−2+3−4+5−6+…+(−1)n+1n.1-2+3-4+5-6 + \ldots + (-1)^{n+1}n.1−2+3−4+5−6+…+(−1)n+1n.

Входные данные
На вход программе подается натуральное число nnn.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Sample Input 1:

1

Sample Output 1:

1

Sample Input 2:

5

Sample Output 2:

3

Sample Input 3:

3

Sample Output 3:

2

'''

n = int(input().strip())
s = 0

for i in range(1, n+1):
    s += ((-1)**(i+1)) * i
print(s)
