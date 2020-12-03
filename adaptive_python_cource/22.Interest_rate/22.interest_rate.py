'''


The interest rate on the deposit is P percent per annum, which are added to the deposit amount after one year. The deposit is X dollars Y cents. Find the size of the deposit in K years.

Input data format

Integers P, X, Y, K.

Output data format

The program should output two numbers: the size of the deposit in K years in dollars and cents. Fractional parts of cents after a year should be discarded. Recalculation of the deposit amount (discarding the fractional parts of cents) occurs annually.

Note: If you are facing issues with accuracy in this problem – try to solve it using only integer numbers.

Sample Input:

12
179
0
5

Sample Output:

315 43

'''

def year_up(p, d, c):
    # доллары + проценты долларовые
    d1 = d + d*p//100
    # центы + проценты по центам
    c1 = c + c*p/100
    # центы с процентов от долларов
    c1 += (d*p) % 100
    # добавили к долларам те доллары, что получились из центов (200 центов = 2 доллара)
    d1 += c1 // 100
    # оставили в центах то, что осталось после добавления основной части в доллары
    c1 = c1 % 100
    return [int(d1), int(c1)] 

depo = dict()

try:
    # percent of bank depo 
    interest = int(input().strip())
    # dollars
    #depo['dollars'] = int(input().strip())
    dollars = int(input().strip())
    # cents
    #depo['cents'] = int(input().strip())
    cents = int(input().strip())
    # years
    years = int(input().strip())
    # tuple, d and c
    money = [dollars, cents]
    
    for i in range(years): 
        money = year_up(interest, money[0], money[1])
        
    print(*money)
    
    
except:
    print('Incorrect input.')