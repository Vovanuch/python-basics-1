''' Executing name_function. Вызов функции из млдуля'''
from name_function import formatted_name
print('Please, enter you first and last name, or x for Exit')
while True:
    first_name = input('Please, enter your first name: ')
    if first_name == 'x':
        print('Goodbye!')
        break
    
    last_name = input('Please, enter your last  name: ')
    if last_name == 'x':
        print('Goodbye!')
        break    
        
    result = formatted_name(first_name, last_name)
    print('Your full name is', result)
