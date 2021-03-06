'''
Вид треугольника

Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

Формат входных данных
На вход программе подаются три числа – длины сторон существующего треугольника.

Формат выходных данных
Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

Sample Input 1:

145
145
139

Sample Output 1:

Равнобедренный

Sample Input 2:

59
59
59

Sample Output 2:

Равносторонний

Sample Input 3:

890
199
700

Sample Output 3:

Разносторонний

'''
stor = [0 for i in range(3)]
for i in range(3):
    stor[i] = int(input().strip())

count = [0 for i in range(3)]
for i in range(3):
    count[i] = stor.count(stor[i])
    
#«Равносторонний», «Равнобедренный» или «Разносторонний»
if max(count) == 3:
    print("Равносторонний")
elif max(count) == 2:
    print("Равнобедренный")
elif max(count) == 1:
    print("Разносторонний")