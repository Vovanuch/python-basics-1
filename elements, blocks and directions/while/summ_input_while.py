'''


Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

Sample Input 1:

5
-3
8
4
0

Sample Output 1:

14

Sample Input 2:

0

Sample Output 2:

0


'''


# summ between two numbers
# s1 и s2 - временные суммы.
s1 = 0
s2 = 0
a = int(input())
s1 += a

while (s1 != s2):
	a = int(input())
	s2 = s1
	s1 += a

print(s1)
	
	
