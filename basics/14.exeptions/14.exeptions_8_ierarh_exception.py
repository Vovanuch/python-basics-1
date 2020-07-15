''' exceptions 8.  '''
'''
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
'''

# ZeroDivisionError, ArithmeticError, AssertionError

''' 
#ver 1
try:
    foo()
except ZeroDivisionError as e:
    print(e)
except ArithmeticError as e:
    print(e)
except AssertionError as e:
    print(e)    
'''

#ver 2
try:
    foo()
except ZeroDivisionError as e:
    print('ZeroDivisionError')
except ArithmeticError as e:
    print('ArithmeticError')
except AssertionError as e:
    print('AssertionError')  
