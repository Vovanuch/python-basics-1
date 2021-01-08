'''

Правильный многоугольник

Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны aaa и количеством сторон nnn вычисляется по формуле: S=n⋅a24tg⁡(πn)S = \dfrac{n \cdot a^2}{4\tg \left(\dfrac{\pi}{n}\right)}S=4tg(nπ​)n⋅a2​Даны два числа: натуральное число nnn и вещественное число aaa. Напишите программу, которая находит площадь указанного правильного многоугольника.

Формат входных данных
На вход программе подается два числа nnn и aaa, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести вещественное число – площадь многоугольника.

Sample Input:

3
2.0

Sample Output:

1.7320508075688779

'''
from math import *

n = float(input().strip())
a = float(input().strip())

s = (n * a**2) / (4 * tan(pi/n))
print(s)