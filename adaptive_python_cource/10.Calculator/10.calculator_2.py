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

print ('Please, enter 3 arguments at separate rows: number_1, number_2, operation (+, -, /, *, mod, pow, div):')

str_error_1 = "Division by 0!"
str_error_2 = 'Unknown action or incorrect input data.'
str_error_3 = 'Uncorrect first and/or second argument!'

a, b, action = input().strip(), input().strip(), input().strip()
try:
    a = float(a)
    b = float(b)

    list_action_1 = ['+', '-', '*', '**']
    dict_action_2 = {'/': '/', 'div': '//', 'mod': '%', 'pow': '**', '//': '//', '%': '%'}
    
    if (action in list_action_1):
        res = eval(f'{a} {action} {b}')
        
    elif (action in dict_action_2.keys()):
        if b != 0:
            res = eval(f'{a} {dict_action_2[action]} {b}')
        else:
            res = str_error_1    
    else:
        res = str_error_2
    print(res)
    
except:
    print(str_error_3)
