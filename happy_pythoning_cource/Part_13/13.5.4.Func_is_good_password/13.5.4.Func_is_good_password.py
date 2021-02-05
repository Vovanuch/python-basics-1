'''

Good password 🌶️

Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

    его длина не менее 8 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.

 Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:

True
False

'''



#его длина не менее 8 символов; 
def is_good_len(password):
    return (len(password) >= 8)

#он содержит как минимум одну заглавную букву (верхний регистр); 
def is_capital_symbol(password):
    res = False
    for c in password:
        if 'Z' >= c >= 'A':
            res = True
            break
    return res


#он содержит как минимум одну строчную букву (нижний регистр);
def is_little_symbol(password):
    res = False
    for c in password:
        if 'z' >= c >= 'a':
            res = True
            break
    return res


#он содержит хотя бы одну цифру.
def is_digit_symbol(password):
    res = False
    for c in password:
        if '9' >= c >= '0':
            res = True
            break
    return res


# объявление функции
def is_password_good(password):
    if is_good_len(password) and is_capital_symbol(password) and is_little_symbol(password) and is_digit_symbol(password):
        return True
    return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
print(ord('0'), ord('1'))