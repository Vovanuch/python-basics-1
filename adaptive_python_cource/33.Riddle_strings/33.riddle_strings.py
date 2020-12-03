'''


Here you will learn how to work with strings.

Many of us are familiar with the following child riddle:

A and B sat in the tree.
A had fallen, B was stolen.
What's remaining in the tree?

Write a program, which reads the two names and outputs the poem, in which these names are used instead of A and B.

Input format:
Two names, separated by a line break. First name should replace A, second one – B.

Output format:
Three lines of the poem with replaced A and B.

Sample Input:

X
Y

Sample Output:

X and Y sat in the tree.
X had fallen, Y was stolen.
What's remaining in the tree?


'''
x, y = input().strip(), input().strip()

print(f"{x} and {y} sat in the tree.\n"
f"{x} had fallen, {y} was stolen.\n"
"What's remaining in the tree?")

