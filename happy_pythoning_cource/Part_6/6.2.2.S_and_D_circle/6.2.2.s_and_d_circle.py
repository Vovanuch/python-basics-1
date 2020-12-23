'''

Площадь и длина

Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RRR.

Формат входных данных
На вход программе подается одно вещественное число RRR​.

Формат выходных данных
Программа должна вывести два числа – площадь круга и длину окружности радиуса RRR.

Примечание. Используйте константу math.pi. 

Sample Input 1:

554.6

Sample Output 1:

966294.7126386268
3484.654571361799

Sample Input 2:

3.14

Sample Output 2:

30.974846927333925
19.729201864543903

Sample Input 3:

5.5

Sample Output 3:

95.03317777109125
34.55751918948772

'''
from math import pi

r = float(input().strip())
s = pi*(r**2)
d = 2*pi*r

print(s, d, sep='\n')