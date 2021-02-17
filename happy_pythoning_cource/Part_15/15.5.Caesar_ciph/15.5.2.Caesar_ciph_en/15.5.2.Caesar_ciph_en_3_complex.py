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
import ceasar

def count_alphas(my_word):
    count = 0
    for c in my_word:
        if c.lower() in ceasar.alphabet_en:
            count += 1
    
    return count



print('Введите текст для шифрования:')
text = input()

for word in text.split():
    result_word = ceasar.set_up_low_char(word, ceasar.cesar_gen(word, ceasar.alphabet_en, count_alphas(word)))
    print(result_word, end=' ')
