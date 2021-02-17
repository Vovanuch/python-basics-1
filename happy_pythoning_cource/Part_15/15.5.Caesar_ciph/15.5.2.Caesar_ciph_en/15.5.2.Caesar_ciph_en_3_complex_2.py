'''

Аве, Цезарь 🌶️

На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных 
На вход программе подается строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.

Sample Input 1:

Day, mice. "Year" is a mistake!

Sample Output 1:

Gdb, qmgi. "Ciev" ku b tpzahrl!

Sample Input 2:

my name is Python!

Sample Output 2:

oa reqi ku Veznut!

'''

# Сама функция шифрования
def cesar_gen(my_text, all_symbols, key):
    secret_text = ''
    for c in my_text.lower():
        if c in all_symbols.lower():
            
            i = all_symbols.lower().index(c)
            ciph_i = (i + key) % len(all_symbols)
            secret_text += all_symbols.lower()[ciph_i]
        else:
            secret_text += c
        
    
    return secret_text
    
# Преобразование заглавных в заглавные, строчных в строчные
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


# подсчёт букв в слове (без цифр и знаков препинания)
def count_alphas(my_word, alphabet):
    count = 0
    for c in my_word:
        if c.lower() in alphabet:
            count += 1
            #print(count)
    
    return count

alphabet_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы

print('Введите текст для шифрования:')
text = input()

# шифруем каждое слово во введённм тексте. ПОсле этого выводим его.
for word in text.split():
    result_word = set_up_low_char(word, cesar_gen(word, alphabet_en, count_alphas(word, alphabet_en)))
    print(result_word, end=' ')
