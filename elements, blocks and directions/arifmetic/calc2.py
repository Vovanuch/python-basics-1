"""Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа."""

#1st num
a = float(input())

#2nd num
b = float(input())

#operand
o = input()

if (o=="+"):
	print(a + b)

elif (o=="-"):
	print(a - b)

elif (o=="pow"):
	print(a ** b)

elif (o=="*"):
	print(a * b)

elif (b==0.0) and (o=="/" or o=="%" or o=="mod" or o=="div"):
	print("Деление на 0!")
	
elif (o=="/"):
	print(a / b)

elif (o=="mod"):
	print(a % b)
	
elif (o=="div"):
	print(a // b)

