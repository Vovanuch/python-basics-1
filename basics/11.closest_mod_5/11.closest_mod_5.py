''' division 5


Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

    y больше или равно x
    y делится нацело на 5

Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("


'''

def closest_mod_5(x=5):
    if x%5 == 0:
        print(f'{x} is a good answer!')
        return x
    else:
        print(x, 'is not an answer!', 'Increasing...')
        closest_mod_5(x+1)



a = closest_mod_5(6)
