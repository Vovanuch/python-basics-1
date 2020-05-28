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
b = array([(1, 3, 5 ,7), (2, 4, 6)])

print(*b)
print(b.ndim)
print(*b.shape)
