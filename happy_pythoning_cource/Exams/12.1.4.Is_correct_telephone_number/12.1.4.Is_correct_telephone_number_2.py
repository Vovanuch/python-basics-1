'''

Валидный номер 🌶️🌶️

На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефонным номером. Строка текста является корректным телефонным номером если она имеет формат:

    abc-def-hijk или
    7-abc-def-hijk

где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если строка является корректным телефонным номером и «NO» в противном случае.

Примечание. Телефонный номер должен содержать только цифры и символ -, а количество цифр в каждой группе должны быть правильным.

Sample Input 1:

7-301-447-5820

Sample Output 1:

YES

Sample Input 2:

301-447-5820

Sample Output 2:

YES

Sample Input 3:

301-4477-5820

Sample Output 3:

NO

Sample Input 4:

3X1-447-5820

Sample Output 4:

NO

Sample Input 5:

3014475820

Sample Output 5:

NO

'''
strint_tel_num = input().strip()
list_parts_tel_numbers = strint_tel_num.split('-')

correct_symbols = [str(i) for i in range(10)]
correct_symbols.extend('-')

if len(list_parts_tel_numbers) not in [3, 4]:
    print("NO")
else:
    if len(list_parts_tel_numbers) == 4:
        if list_parts_tel_numbers[0] != '7':
            print("NO")
        if len(str(list_parts_tel_numbers)) != 11:
            print("NO")
        
