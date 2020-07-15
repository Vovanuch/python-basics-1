''' file for import '''

class BadName(Exception):
    pass


def greeting(str_name = 'Man'):
    if str_name[0].isupper():
        print(f'Hello, {str_name}!')
    else:
        raise ValueError(f'Name {str_name} is incorrect. Please, use upper case for 1st letter!')
