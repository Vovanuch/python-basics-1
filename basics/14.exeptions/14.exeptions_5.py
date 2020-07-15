''' exeptions 5 '''
try:
    f = open("my_file")
except IOError as err:
    print('Error:', err)
    print('Code of error', err.errno)
