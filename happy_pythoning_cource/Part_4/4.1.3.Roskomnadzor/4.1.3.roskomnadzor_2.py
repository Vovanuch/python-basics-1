'''

Роскомнадзор

Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.

Формат входных данных
На вход программе подаётся целое число — возраст пользователя.

Формат выходных данных
Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.

Sample Input 1:

16

Sample Output 1:

Доступ запрещен

Sample Input 2:

18

Sample Output 2:

Доступ разрешен

Sample Input 3:

19

Sample Output 3:

Доступ разрешен

'''



print('Доступ разрешен') if int(input()) >= 18 else print('Доступ запрещен')