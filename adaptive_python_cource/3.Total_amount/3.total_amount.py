'''
Write a simple Python program that calculates the final amount of your loan that earns compound interest, given the principal amount, the annual nominal interest rate, the number of times interested is compounded per year, and the number of years.

If P is the principal amount (initial investment), r is the annual nominal interest rate, n is the number of times the interest is compounded per year, and t is the number of years, the total amount paid is

A=P*(1+r/n)^(n*t)

Amount owed is the principal amount multiplied by the amount one plus the annual nominal interest rate divided by n raised to the number of times compounded multiplied by the number of years. (exponentiation)

Careful! The rules of precedence really matter in the student loan calculator problem.
'''

p = float(input())
r = float(input())
n = float(input())
t = float(input())

total_amount = p * (1 + (r / n))**(n*t)

print(total_amount)
