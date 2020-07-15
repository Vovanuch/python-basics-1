''' exeptions 3.1 another way '''

def division(x, y):
    try:
        result = x / y
    except Exception as e:
        print('Sorry, something goes wrong..')
        print(e)
    else:
        print(f'Result is: {result}')
    finally:
        print('Thank you! See you later!')

print('6, 2 :')        
division(6, 2)
print('6, []')
division(6, [])
print('6, 0')
division(6, 0)
