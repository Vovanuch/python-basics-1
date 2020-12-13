'''


Robot

The robot moves down the office in the Bioinformatics Institute. Recently, students from the programmers group wrote a program for this robot, according to which when robot enters the room, he counts the number of programmers present in this room and says it aloud: "n programmers".

In order for it to sound correctly, for each n n n you need to use the correct word ending.

Write a program, reading an integer n n n (non-negative one) from the user input, outputting this number together with the correctly changed word "programmer", so that the robot could correctly communicate with people, for example: 1 programmer, 2 programmers, 5 programmers.

There can be many programmers in one room. Make sure that your program works correctly for all the cases until 1000 persons

Sample Input 1:

5

Sample Output 1:

5 programmers

Sample Input 2:

0

Sample Output 2:

0 programmers

Sample Input 3:

1

Sample Output 3:

1 programmer

Sample Input 4:

2

Sample Output 4:

2 programmers

'''

n = int(input().strip())
pr = 'programmer'
s = 's'
if n != 1:
    print(f'{n} programmers')
else:
    print(f'{n} programmer')