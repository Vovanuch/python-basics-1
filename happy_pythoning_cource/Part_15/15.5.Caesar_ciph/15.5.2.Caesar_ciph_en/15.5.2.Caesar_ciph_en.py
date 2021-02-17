'''

Зашифруйте текст "To be, or not to be, that is the question!" алгоритмом Цезаря с сдвигом вправо на 17 символов.
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
            

# alpha = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#en_alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)] # СПИСОК! Не строка. для нижнего регистра.
const_lower_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы
#print(const_lower_en)

print('Введите текст для шифрования:')
text = input()
print('Введите сдвиг (целое число):')
n = int(input().strip())

result = cesar_gen(text, const_lower_en, n)
result_with_up = set_up_low_char(text, result)
print(result_with_up)
