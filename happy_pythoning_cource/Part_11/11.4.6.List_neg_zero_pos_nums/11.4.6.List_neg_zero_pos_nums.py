'''

Negatives, Zeros and Positives

На вход программе подается натуральное число nnn, а затем nnn целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

7
3
-4
1
0
-1
0
-2

Sample Output 1:

-4
-1
-2
0
0
3
1

Sample Input 2:

5
4
3
-2
-10
0

Sample Output 2:

-2
-10
0
4
3

'''

n = int(input().strip())
lisr_neg_num = []
lisr_zero = []
lisr_pos_num = []

# create list from input
for i in range(n):
    x = int(input().strip())
    if x < 0:
        lisr_neg_num.append(x)
    elif x == 0:
        lisr_zero.append(x)
    else:
        lisr_pos_num.append(x)
        
print(*lisr_neg_num, sep='\n')
print(*lisr_zero, sep='\n')
print(*lisr_pos_num, sep='\n')