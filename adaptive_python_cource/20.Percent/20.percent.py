'''


Write a program which finds the percentage of students who have received the A grade.

Used the five-point grading scale with grades A, B, C, D and F.

Input format:
A single line with student grades separated by a space. There is at least one grade.

Output format:
The floating point number with exactly two digits after the decimal point.

Sample Input 1:

F B A A B C A D

Sample Output 1:

0.38

Sample Input 2:

B C B

Sample Output 2:

0.00

Sample Input 3:

A D

Sample Output 3:

0.50

'''


try:
    #
    list_grades = input().strip().split()
    count_a = list_grades.count("A")
    count_grades = len(list_grades)
    percent_a = count_a / count_grades
    print(f'{percent_a:.2f}')
    #print(round(percent_a, 2)) - not exactly 2 digits aster decimal
    '''
    >>> v=10.4
    >>> print('% 6.2f' % v)
    10.40
    >>> print('% 12.1f' % v)
    10.4
    >>> print('%012.1f' % v)
    0000000010.4
'''
    
except:
    print('Incorrect input.')