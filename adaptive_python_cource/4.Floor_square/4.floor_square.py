'''


Floor-space of the room

Residents of the Malevia country often experiment with the plan of their rooms. Rooms can be triangular, rectangular and round. To quickly calculate the floorage it is required to write a program, which gets the type of the room shape and the relevant parameters as input - the program should output the area of the resulting room.

The value of 3.14 is used instead of the number π in Malevia.

Input format used by the Malevians:

triangle
a
b
c

where a, b and c — lengths of the triangle sides.

rectangle
a
b

where a and b —lengths of the rectangle sides.

circle
r

where r — circle radius.

Sample Input 1:

rectangle
4
10

Sample Output 1:

40.0

Sample Input 2:

circle
5

Sample Output 2:

78.5

Sample Input 3:

triangle
3
4
5

Sample Output 3:

6.0


'''
def get_s_room(form):
    if form == 'rectangle':
        a, b = float(input()),float(input())
        return a*b
    if form == 'triangle':
        a, b, c = float(input()),float(input()), float(input())
        p = (a + b + c) / 2
        s = (p * (p-a) * (p-b) * (p-c))**(0.5)
        return s
    if form == 'circle':
        r = float(input())
        pi = 3.14
        s = pi * r**2
        return s
    
form = input()
print(get_s_room(form))