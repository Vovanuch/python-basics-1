'''

Символы всех строк

На вход программе подается натуральное число nnn, а затем nnn строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из символов всех введенных строк.

Примечание. В результирующем списке могут содержаться одинаковые символы.

Sample Input:

3
abc
def
ghi

Sample Output:

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

'''


# how much rows
n = int(input().strip())
list_strings = []
list_chars = []

# create list from input
for i in range(n):
    list_strings.append(input().strip())

# create list of chars
for i in range(n):
    list_chars.extend(list_strings[i])
    
print(list_chars)