'''

Звездный треугольник

Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;

а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.

Sample Input 1:

*
9

Sample Output 1:

*
**
***
****
*****
****
***
**
*

Sample Input 2:

+
5

Sample Output 2:

+
++
+++
++
+

Sample Input 3:

?
7

Sample Output 3:

?
??
???
????
???
??
?

'''

# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base):
        print(fill * i)
    for i in range(base, 0, -1):
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
