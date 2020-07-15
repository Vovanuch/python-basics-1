''' exeptions 3 '''

def division(x, y):
    try:
        return x / y
    except TypeError:
        return ('Type error!')
    except ZeroDivisionError:
        return 'You can not divide by zero!'
    except:
        return 'Unknown error'
    #можно перечислить типы исключений в кортеже:
    #except (TypeError, ZeroDivisionError, IndexError)
        
print('6, 2: ', division(6, 2))
print('6, a:', division(6, 'a'))
print('6, 0: ', division(6, 0))


# второй вариант исключений - делать прямо при вызове.
try:
    a = division(1, 2, 3)
    print(a)
except Exception as e:
    print('Unknown error in strarting function.')
    print('Type of exception:',type(e))
    print('Text: ', e)
    #raise
