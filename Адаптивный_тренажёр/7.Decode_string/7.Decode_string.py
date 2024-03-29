'''


Кодирование длин серий — это базовый алгоритм сжатия данных.

В этой задаче мы реализуем алгоритм дешифровки строк, закодированных с помощью одного из самых простых  вариантов кодирования длин серий.

На вход алгоритму подаётся строка, содержащая цифры и символы латинского алфавита. Эта строка разбивается на так называемые "серии", которые кодируются парой число-символ или просто символ (в таком случае число считается равным единице). Результат должен содержать эти серии в том же порядке, что они и встречаются в исходной строке, при этом каждая серия раскрывается в последовательность символов соответствующей длины. 

Например, рассмотрим строку 

3ab4c2CaB

Разобъём её на серии

3a b 4c 2C a B

После чего преобразуем серии и получим исходную закодированную строку:

aaabccccCCaB

Формат ввода:
Одна строка, содержащая закодированную последовательность.

Формат вывода:
Строка, содержащая раскодированную последовательность.

Sample Input:

3ab4c2CaB

Sample Output:

aaabccccCCaB

'''
def decode_str(my_string):
    my_len = len(my_string)
    res = ''
    for i in range(my_len, 0, -1):
        #print(my_string[-i], sep='', end='')
        if my_string[-i].isdigit() and (i != my_len):
            res = my_string[:(i)] + int(my_string[-i])*my_string[-i+1]# + my_string[-i+2:]
            
    return res


s = input().strip()
print(decode_str(s))
