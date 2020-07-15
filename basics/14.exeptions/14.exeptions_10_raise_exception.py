''' exceptions 10. Raise exception '''

class BadName(Exception):
    pass


def greeting(str_name = 'Man'):
    if str_name[0].isupper():
        print(f'Hello, {str_name}!')
    else:
        raise ValueError(f'Name {str_name} is incorrect. Please, use upper case for 1st letter!')
        #raise BadName(f'Name {str_name} is incorrect. Please, use upper case for 1st letter!')
        

while True:
    try:
        greeting(input('Please, enter the name of guy you want to greed: '))
        
    except ValueError:
        print('Try again, please! Enter correct name!')
        
    else:
        break
