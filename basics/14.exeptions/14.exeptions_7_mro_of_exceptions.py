''' exeptions 7. mro for exceptions  '''

try:
    15 / 0
except ZeroDivisionError as zd:
    print('There is an ZeroDivisionError exception.')
    #print(zd.mro())
    print(zd)
    print(zd.args)

print(ZeroDivisionError.mro())
