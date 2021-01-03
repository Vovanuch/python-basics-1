'''

Вторая цифра

Дано натуральное число n (n>9)n \, (n > 9)n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

Формат входных данных 
На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.

Формат выходных данных
Программа должна вывести его вторую (с начала) цифру.

Sample Input 1:

455672

Sample Output 1:

5

Sample Input 2:

59

Sample Output 2:

9

Sample Input 3:

123

Sample Output 3:

2

'''

# 1st way, easy and fast
#n = input().strip()
#print(list(n)[1])

# 2nd way, long and boring 
n = input().strip()
d1 = int(n) // 10 ** (len(n) - 2)
d2 = d1 % 10
print(d2)