#a, b, c - sides of triangle
a = int(input())
b = int(input())
c = int(input())
#p is a half of perimentr
p = (a+b+c)/2
#S is a square of triangle ic accordance with Geron formula, blin.)
S = (p*(p-a)*(p-b)*(p-c))**0.5
print(S)


