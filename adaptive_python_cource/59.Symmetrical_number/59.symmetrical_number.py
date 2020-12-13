'''


Symmetrical number

Given a four-digit number. Determine whether its decimal notation is symmetric. If the number is symmetrical, output 1, otherwise output any other integer. The number may have less than four digits, then you should assume that its decimal notation is complemented by insignificant zeros on the left.

Sample Input 1:

2002

Sample Output 1:

1

Sample Input 2:

2008

Sample Output 2:

37

'''

def is_symmetrical(my_str):
    if (my_str[0] == my_str[3]) and (my_str[1] == my_str[2]):
        return 1
    else:
        return 0


s = input().strip()
if len(s) < 4:
    while (len(s) < 4):
        s = '0' + s

if len(s) == 4:
    print(is_symmetrical(s))

    
