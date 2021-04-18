'''


In the Roman numeral system, the following symbols are used to represent numbers (on the right are the numbers, which correspond to these symbols in the decimal system):

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


We will use a notation in which the numbers 4, 9, 40, 90, 400 and 900 are represented as a subtraction of a smaller number from a larger one: IV, IX, XL, XC, CD and CM, respectively.

Given the natural number n n n, 0<n<4000 0 \lt n \lt 4000 0<n<4000.

Find the string which represents this number in the Roman numeral system.

Sample Input 1:

1984

Sample Output 1:

MCMLXXXIV

Sample Input 2:

9

Sample Output 2:

IX

Sample Input 3:

3

Sample Output 3:

III

'''
dict_nums_rome_arabic = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
dict_ex1 = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

dict_nums_arabic_rome = {v:k  for k,v in dict_nums_rome_arabic.items()}

n = int(input().strip())
