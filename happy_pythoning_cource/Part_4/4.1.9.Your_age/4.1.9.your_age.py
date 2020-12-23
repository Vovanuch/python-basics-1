'''

Возрастная группа

Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

    до 13 включительно – детство;
    от 14 до 24 – молодость;
    от 25 до 59 – зрелость;
    от 60 – старость.

Формат входных данных
На вход программе подаётся одно целое число – возраст пользователя.

Формат выходных данных
Программа должна вывести название возрастной группы.

Sample Input 1:

4

Sample Output 1:

детство

Sample Input 2:

91

Sample Output 2:

старость

Sample Input 3:

40

Sample Output 3:

зрелость

'''
try:
    age = int(input().strip())
except:
    age = -1
    print('Entered age is incorrect')

periods = ['детство', 'молодость', 'зрелость', 'старость']

if age in range(0, 14):
    print(f'{periods[0]}')
elif age in range(14, 25):
    print(f'{periods[1]}')
elif age in range(25, 60):
    print(f'{periods[2]}')
elif age > 69:
    print(f'{periods[3]}')
else:
    print('incorrect data.')
'''
до 13 включительно – детство;
от 14 до 24 – молодость;
от 25 до 59 – зрелость;
от 60 – старость.
'''