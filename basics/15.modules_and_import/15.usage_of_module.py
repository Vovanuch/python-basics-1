''' main file, where we use imported exception'''

import imported_exception

str_name = input('Enter your name, please: ')
imported_exception.greeting(str_name)

print(imported_exception.greeting('Vladimir'))
