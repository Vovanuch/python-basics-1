'''

Палиндром 🌶️

Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))

должен выводить:

True
True
False

'''

# объявление функции
def is_palindrome(text):
    list_del_symbols = [',', '.', '!', '?', '-', ' ']
    list_text = []
    for c in text:
        if c not in list_del_symbols:
            list_text.extend(c.lower())
    
    if list_text == list_text[::-1]:
        return True
    return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))