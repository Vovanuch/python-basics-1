# working with numpy
from numpy import *

# создание одномерного массива
a = array([2,3,4])
print(*a)

#размерность массива - этот массив одномерный, результат - 1
print(a.ndim)

#размер массива - в этом массиве 3 элемента
print(*a.shape)


#второй массив, двумерный
b = array([(1.3, 5 ,7), (2, 4, 6)])

print(b)
print('Dimentions: ', b.ndim)
print('Count of rows and columns', *b.shape)

print('Array size (len):',b.size)
print()

# array with zero-initialized items
print('Array with zero-initialized items')
z = zeros((3, 2))
print(z)

print()
#arange - generate array by using range
arr = arange(1, 20, 3)
print('arange result: ', arr)

print()
print('linspace:')
#linspace - генерирует массив с заданным количеством точек между границами
lin = linspace(1, 10, 20)
print(lin)

print()
#преобразование одномерного массива в двумерный
# но кол-во элементов в одномерном массиве должно укладываться в двумерный. 15 нельзя преобразовать в 4, 3.
c = arange(12).reshape(4, 3)
print(c)

#операции над массивами - поэлементно
print()
a = array([5, 10, 15])
b = arange(1, 4)
print('a:', a)
print('b:', b)
print('a + b:', a + b) 
print('a - b:', a - b) 
print('a * b:', a * b) 
print('a / b:', a / b) 
print('a**2:', a ** 2) 

#проверяем каждый элемент на условие
print()
print('a < 10', a < 10)
