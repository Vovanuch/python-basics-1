'''
Генерация и проверка безопасного пароля.
'''

import random

def return_bool(text):
    if text.lower() in ['y', 'yes', 'да', 'д']:
        return True
    return False

def add_needed_symbols(text, my_str, flag):
    if flag == True:
        text += my_str
    return text


def remove_needed_symbols(text, my_str, flag):
    if flag == True:
        for c in my_str:
            text.replace(c, '')
    return text


def generate_password(my_chars, len_of_pass):
    #password = random.sample(my_chars, len_of_pass)
    password = ''
    for i in range(len_of_pass):
        password += random.choice(my_chars)
    
    return str(password)

def convert_list_str(my_list):
    s = ''
    for e in my_list:
        s += e
    return s


digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
tehno = '!#$%&*+-=?@^_'
chars = ''
excluding = 'il1Lo0O'
list_of_passwords = []


pass_count = int(input('Сколько паролей необходимо сгенерировать? '))
pass_len = int(input('Какая должна быть длина пароля? '))
pass_include_digits = return_bool(input('Включать ли цифры? Д/Н '))
pass_include_uppers = return_bool(input('Включать ли символы верхнего регистра? Д/Н '))
pass_include_lowers = return_bool(input('Включать ли символы нижнего регистра? Д/Н '))
pass_include_tehno = return_bool(input('Включать ли технические символы? Д/Н '))
pass_exclude_unnormal = return_bool(input(f'Исключать ли неоднозначные символы {excluding}? Д/Н '))

chars = add_needed_symbols(chars, digits, pass_include_digits)
chars = add_needed_symbols(chars, lowercase_letters, pass_include_lowers)
chars = add_needed_symbols(chars, uppercase_letters, pass_include_uppers)
chars = add_needed_symbols(chars, tehno, pass_include_tehno)
chars = remove_needed_symbols(chars, excluding, pass_exclude_unnormal)

for i in range(pass_count):
    list_of_passwords.append(generate_password(chars, pass_len))
    

print(f'Generated passwords are:')
for p in list_of_passwords:
    print(p)
    #print(*p, sep='')
    #s = convert_list_str(s)
    #s = ''.join(str(e) for e in p)
    #print(f'Generated password is {s}')