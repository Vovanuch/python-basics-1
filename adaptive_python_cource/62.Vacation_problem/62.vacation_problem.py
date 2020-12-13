'''


Write a Python program to figure out what day you would return, given the day you leave and how many days you will be gone.
For example:

    If you leave on a Friday and you are gone for two (2) days, you would return on a Sunday.
    If you leave on a Monday and you are gone for eight (8) days, you would return on a Tuesday.
    If you leave on a Wednesday and you are gone 23 days, you would return on a Friday. 

The program should ask for the day to leave and how many days the person will be away.

A sample conversation should look like:
What day are you leaving? Wednesday
How many days will you be gone? 32
If you left on Wednesday and returned 32 days later, you would return on Sunday

One way to attack this problem is convert the days into numbers. For example, 0 = Sunday, 1 = Monday, and so on until 6 = Saturday. You might use a way to find the remainder to solve the vacation problem.

Sample Input 1:

Friday
19

Sample Output 1:

If you leave on Friday and return 19 days later, you will return on Wednesday.

Sample Input 2:

Wednesday
64

Sample Output 2:

If you leave on Wednesday and return 64 days later, you will return on Thursday.

Sample Input 3:

Monday
10

Sample Output 3:

If you leave on Monday and return 10 days later, you will return on Thursday.

'''
# Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
dict_days_1 = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
dict_days_2 = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6}

day_vacation_begin = input().strip()
day_count = int(input().strip())
a = (dict_days_2[day_vacation_begin] + day_count) % 7
day_vacation_end = dict_days_1[a]

str_return = f"If you leave on {day_vacation_begin} and return {day_count} days later, you will return on {day_vacation_end}."

print(str_return)