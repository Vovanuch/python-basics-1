'''

k-ая буква слова 🌶️🌶️

На вход программе подается натуральное число nnn и nnn строк, а затем число kkk. Напишите программу, которая выводит kkk-ую букву из введенных строк на одной строке без пробелов.

Формат входных данных
На вход программе подается натуральное число nnn,  далее nnn строк, каждая на отдельной строке. В конце вводится натуральное число kkk – номер буквы (нумерация начинается с единицы).

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.

Sample Input:

5
abcdef
bcdefg
cdefgh
defghi
efghij
2

Sample Output:

bcdef

'''

# how much rows
n = int(input().strip())
list_strings = []

# create list from input
for i in range(n):
    list_strings.append(input().strip())

# position of chars
k = int(input().strip())

# res - resulted string
res = ''
for i in range(n):
    if len(list_strings[i]) >= k:
        res += list_strings[i][k-1]
        
print(res)