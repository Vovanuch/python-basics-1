'''

Задача Иосифа Флавия 🌶️

nnn человек, пронумерованных числами от 111 до nnn, стоят в кругу. Они начинают считаться, каждый kkk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа nnn и kkk, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.

Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно тут.

Примечание 2. Визуализацию работы алгоритма можно посмотреть тут.

Sample Input 1:

2
1

Sample Output 1:

2

Sample Input 2:

5
2

Sample Output 2:

3

Sample Input 3:

7
5

Sample Output 3:

6

'''

def get_last_elem(my_list, start, step):
    if len(my_list) < 2:
        return my_list
    
    ind = (step - 1) % len(my_list)
    my_list.pop(ind)
    my_list = my_list[ind:] + my_list[:ind]
    return get_last_elem(my_list, start, step)

index = 0
n, k = int(input().strip()), int(input().strip())
list_n = [i for i in range(1, n+1)]

print(*get_last_elem(list_n, 0, k)) 