'''

Шифр Цезаря 🌶️

Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.

Формат входных данных
В первой строке дается число n  (1≤ n≤ 25)n \, (1 \le n \le 25)n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.

Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение, а не закодировать.

Sample Input 1:

1
bwfusvfupdbftbs

Sample Output 1:

avetruetocaesar

Sample Input 2:

14
fsfftsfufksttskskt

Sample Output 2:

rerrfergrweffewewf

'''
def decode(my_str, n):
    res = ''
    for c in my_str:
        if ord(c)-n < 97:
            x = ord(c)-n%26 + 26
        else:
            x = ord(c)-n%26
        
        print(x)
        res += chr(x)
    
    return res

n = int(input().strip())
s = input().strip()
result_str = decode(s, n)
print(result_str)