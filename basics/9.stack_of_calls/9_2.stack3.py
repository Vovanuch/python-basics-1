'''

В процессе выполнения кода на стек добавляются и со стека снимаются функции. Добавление функции на стек увеличивает его размер на 1, снятие функции со стека уменьшает его размер на 1.

Чему равен максимальный размер стека в процессе выполнения следующего кода?
Обратите внимание, что при интерпретации кода на стеке находится функция module, которую также нужно учесть при подсчете размера стека.
В рамках данного задания можно считать, что функция print ﻿не вызывает дополнительных функций внутри себя.

'''

def a():
    print('I\'m a function a!')
    
def b(x):
    x()
    
def c():
    a()

b(c)
