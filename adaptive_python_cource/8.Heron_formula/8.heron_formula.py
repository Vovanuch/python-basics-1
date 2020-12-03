'''

Heron's formula

Many years ago when Paul went to school, he did not like the Heron's formula to calculate the area of a triangle, because he considered it very complex. Once he decided to help all school students: to write and distribute the program, calculating the area of a triangle by its three sides.

However, there was a problem: as Paul did not like the formula, he did not memorize it. Help him finish this act of kindness and write the program, calculating the area of a triangle by the transferred length of its sides, in accordance with the Heron's formula:
S=p(p−a)(p−b)(p−c) S=\sqrt{p(p−a)(p−b)(p−c)} S=p(p−a)(p−b)(p−c)
​ where p=a+b+c2 p=\dfrac{a+b+c}2 p=2a+b+c​ – half-perimeter of the triangle. On the input, the program has integers, and the output should be a real number corresponding to the area of the triangle.

Sample Input:

3
4
5

Sample Output:

6.0

'''
sides = []
for i in range(3):
    sides.append(int(input().strip()))

# half of perimetr
p = sum(sides)/2
# square
s = (p * (p-sides[0]) * (p-sides[1]) * (p-sides[2]))**(0.5)
print(s)