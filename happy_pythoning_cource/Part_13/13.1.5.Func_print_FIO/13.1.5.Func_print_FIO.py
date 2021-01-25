'''

ФИО

Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

    name – имя человека;
    surname – фамилия человека;
    patronymic – отчество человека;

а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

Sample Input 1:

Александр
Пушкин
Сергеевич

Sample Output 1:

ПАС

Sample Input 2:

тимур
Гуев
ахсарбекович

Sample Output 2:

ГТА

'''

def print_fio(list_names):
    res = ''
    for name in list_names:
        res += name[0].upper()
    print(res)

list_names = [input().strip() for _ in range(3)]

print_fio(list_names)