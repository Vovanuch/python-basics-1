'''
На easy

На вход программе подаются два целых числа aaa и bbb. Напишите программу, которая выводит:

    сумму чисел aaa и bbb;
    разность чисел aaa и bbb;
    произведение чисел aaa и bbb;
    частное чисел aaa и bbb;
    целую часть от деления числа aaa на bbb;
    остаток от деления числа aaa на bbb;
    корень квадратный из суммы их 101010-х степеней: a10+b10\sqrt{a^{10} + b^{10}}a10+b10

    ​.

Формат входных данных
На вход программе подаются два целых числа aaa и b (b≠0)b \, (b \neq 0)b(b=0), каждое на отдельной строке.

Формат выходных данных
Программа должна вывести результаты математических операций в соответствии с условием задачи.

Sample Input 1:

3
8

Sample Output 1:

11
-5
24
0.375
0
3
32768.90100384814

Sample Input 2:

123
2

Sample Output 2:

125
121
246
61.5
61
1
28153056843.0

Sample Input 3:

454
322

Sample Output 3:

776
132
146188
1.4099378881987579
1
132
19595820067580.043

'''

a, b = int(input().strip()), int(input().strip())
summa = a + b
razn = a - b
multi = a * b
chasn = a / b
cel = a // b
ost = a % b
res = ((a ** 10) + (b ** 10)) ** 0.5

print(summa)
print(razn)
print(multi)
print(chasn)
print(cel)
print(ost)
print(res)
