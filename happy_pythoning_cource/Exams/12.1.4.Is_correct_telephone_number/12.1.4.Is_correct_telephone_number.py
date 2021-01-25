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

def is_correct_format_small(tel_str):
    is_correct = False
    if len(tel_str) == 12:
        if (tel_str[3] =='-') and (tel_str[7] =='-'):
            try:
                part_1 = int(tel_str[0:3])
                part_2 = int(tel_str[4:7])
                part_3 = int(tel_str[8:])
                is_correct = True
            except:
                is_correct = False
    return is_correct

def is_correct_format_large(tel_str):
    is_correct = False
    if tel_str[0:2] == '7-' and is_correct_format_small(tel_str[2:]):
        return True
    else:
        return False


string_tel_number = input().strip()
if is_correct_format_small(string_tel_number) or is_correct_format_large(string_tel_number):
    print('YES')
else:
    print('NO')