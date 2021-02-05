'''
BEEGEEK

BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.

Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False
'''
# объявление функции проверки чётности
def is_chetn(num):
    if num%2 == 0:
        return True
    return False

# объявление функции проверки простоты
def is_prime(num):
    if (num == 1):
        return False
    
    for i in range(2, num):
        if (num % i == 0) :
            return False
    return True


# объявление функции проверки палиндромности
def is_palindrome(text):
    list_del_symbols = [',', '.', '!', '?', '-', ' ']
    list_text = []
    for c in str(text):
        if c not in list_del_symbols:
            list_text.extend(c.lower())
    
    if list_text == list_text[::-1]:
        return True
    return False


# объявление функции
def is_valid_password(password):
    list_nums = [int(s) for s in password.split(':')]
    if len(list_nums) == 3:
        if is_palindrome(list_nums[0]):
            if is_prime(list_nums[1]):
                if is_chetn(list_nums[2]):
                    return True
    return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))