'''


Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.

Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.

Формат ввода:

Два слова, каждое на отдельной строке. 
Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.

Формат вывода:
True или False.

Sample Input 1:

silent
listen

Sample Output 1:

True

Sample Input 2:

AbaCa
AcaBa

Sample Output 2:

True

Sample Input 3:

abaca
acada

Sample Output 3:

False



'''

s1, s2 = input(), input()

list1 = sorted(list(s1.lower()))
list2 = sorted(list(s2.lower()))


if list1 == list2:
    print('True')
else:
    print('False')