'''

Standard American Convention

На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.

Формат входных данных
На вход программе подаётся натуральное число n, (0<n<10100)n, \, (0 < n < 10^{100})n,(0<n<10100).

Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи.

Sample Input 1:

1000000

Sample Output 1:

1,000,000

Sample Input 2:

100

Sample Output 2:

100

Sample Input 3:

12345

Sample Output 3:

12,345

'''
def insert_symbol(my_list, my_symb):
    if len(my_list) < 4:
        return my_list
    
    add = 0
    i = 3
    my_list = my_list[::-1]
    #while i < len(my_list):
    for i in range(3, len(my_list), 3):
        my_list.insert(i + add, my_symb)
        add += 1
    my_list = my_list[::-1]
    return my_list
    

s = input().strip()
list_s = list(s)

list_s = insert_symbol(list_s, ',')

print(*list_s, sep='')

