'''


Write a program, which reads the number of direction (1 – up, 2 – down, 3 – left, 4 – right, 0 – stay) and outputs the text «move up» (or «move down», or «move left», or «move right», or «do not move» depending on the entered number). If it is a number that does not belong to any of the listed directions, the program should output: «error!»

Note: the output text should exactly match the sample! Including letters case and location of spaces.

Sample Input:

1

Sample Output:

move up

'''


try:
    s = int(input().strip())
    d = {1:"move up", 2:"move down", 3:"move left", 4:"move right", 0:"do not move"}
    if s not in d.keys():
        print('error!')
    else:
        print(d[s])

except:
    print('error!')