'''


Calculator

Write a simple calculator that reads the three input lines: the first number, the second number and the operation, after which it applies the operation to the entered numbers ("first number" "operation" "second number") and outputs the result to the screen. Note that the numbers can be real.

Supported operations: +, -, /, *, mod, pow, div; where
mod — taking the residue,
pow — exponentiation,
div — integer division.

If a user performs the division and the second number is 0, it is necessary to output the line "Division by 0!".

Sample Input 1:

5.0
0.0
mod

Sample Output 1:

Division by 0!

Sample Input 2:

-12.0
-8.0
*

Sample Output 2:

96.0

Sample Input 3:

5.0
10.0
/

Sample Output 3:

0.5

'''

str_error = "Division by 0!"
a, b, action = float(input().strip()), float(input().strip()), input().strip()

# +, -, /, *, mod, pow, div
if action == '+':
    res = a + b
elif action == '-':
    res = a - b
elif action == '/':
    if b != 0:
        res = a / b
    else:
        res = str_error
elif action == '*':
    res = a * b
elif action == 'mod':
    if b != 0:
        res = a % b
    else:
        res = str_error
elif action == 'div':
    if b != 0:
        res = a // b
    else:
        res = str_error
elif action == 'pow':
    res = a ** b
else:
    res = 'unknown action!'

print(res)