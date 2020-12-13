'''


You should write a program that can transform some units of measurement into others.

The following transformations should be supported:

    miles (1 mile = 1609 m),
    yards (1 yard = 0.9144 m),
    feet (1 foot = 30.48 cm),
    inches (1 inch = 2.54 cm),
    kilometres (1 km = 1000 m),
    meters (m),
    centimetres (1 cm = 0.01 m)
    millimetres (1 mm = 0.001 m)

Use the units of measurement specified in the problem description with the exact specified accuracy.

Input format:
Single line in the following format:
<number> <unit_from> in <unit_to>
For example: if you get the line "15.5 mile in km", then you should transform 15.5 miles into kilometers.

Output format:
Real number in scientific format (exponential), with an accuracy of exactly two digits after decimal point.

Sample Input:

15.5 mile in km

Sample Output:

2.49e+01

'''
#list_unit = ['mile', 'yard', 'foot', 'inch', 'km', 'm', 'cm', 'mm']
dict_unit = {'mile':1609, 'yard':0.9144, 'foot':0.3048, 'inch':0.0254, 'km':1000, 'm':1, 'cm':0.01, 'mm':0.001}

list_input = input().strip().split()
mnogitel = float(list_input[0])
unit_from = list_input[1] 
unit_to = list_input[3] 
#print(list_input)

total_len = mnogitel * dict_unit[unit_from] / dict_unit[unit_to] 
'''
>>> "{:.2E}".format(Decimal('40800000000.00000000000000'))
'4.08E+10'

Instead of format, you can also use f-strings:

>>> f"{Decimal('40800000000.00000000000000'):.2E}"
'4.08E+10'
'''

print(f"{total_len:.2e}")
