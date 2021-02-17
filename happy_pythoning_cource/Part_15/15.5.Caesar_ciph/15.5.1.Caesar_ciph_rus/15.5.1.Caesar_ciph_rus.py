'''


Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря с сдвигом вправо на 101010 символов.

Примечание. Считайте, что русский алфавит состоит из 323232 букв (буква ё отсутствует).

 y=(x+k) mod n, x=(y−k) mod n, 
 где xxx — символ открытого текста, yyy — символ шифрованного текста, nnn — мощность алфавита (количество символов), а kkk — ключ.

Исходный алфавит: А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я

'''

def cesar_gen(my_text, all_symbols, key):
    secret_text = ''
    for c in text.lower():
        if c in all_symbols.lower():
            i = all_symbols.lower().index(c)
            ciph_i = (i + key) % len(all_symbols)
            secret_text += all_symbols.lower()[ciph_i]
        else:
            secret_text += c
    
    return secret_text
    

def set_up_low_char(open_str, sec_str):
    res = ''
    for i in range(len(open_str)):
        #print(open_str[i], sec_str[i])
        if open_str[i].upper() == open_str[i]:
            res += sec_str[i].upper()
            #print(res)
        else:
            res += sec_str[i]
            
    return res
            

alpha = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# rus_alphabet = [x for x in range(ord('а'), ord('я') + 1) # для нижнего регистра.


print('Введите текст для шифрования:')
text = input()
print('Введите сдвиг (целое число):')
n = int(input().strip())

result = cesar_gen(text, alpha, n)
result_with_up = set_up_low_char(text, result)
print(result_with_up)
