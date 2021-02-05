'''
Бросание двух игральных кубиков с возможностью повторить бросок. 
'''
import random

again = 'д'
while again.lower() == 'д' or again.lower() == 'да':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')

    if again == 'Да' or again == 'да':
        print('Так уж и быть, бросим еще раз.')
    else:
        print('Игра окончена')