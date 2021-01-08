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
fsfftsfufksttsksk

Sample Output 2:

rerrfergrweffewewf

'''
def act(my_str, n, alphavit, action):
    res = ''
    if action.lower() == 'c':
        koef = 1
    elif action.lower() == 'd':
        koef = -1
    else:
        print('Incorrect type of action.')
        return 'Error'
    
    for c in my_str:
        res += alphavit[ (alphavit.find(c) + (n * koef)) % len(alphavit) ] #
    return res


alphavit = 'abcdefghijklmnopqrstuvwxyz'

print('This is a simple Caesar algoritm.')
type_of_action = input('Please, choose your action: to code / to decode message. C - code, D - decode: ')

n = int(input('Please, enter number of slicing (3 as example): ').strip())

print('Please, enter your text for encoding/decoding:')
s = input().strip()
result_str = act(s, n, alphavit, type_of_action)
print('Your resulted text is:\n', result_str, sep='')