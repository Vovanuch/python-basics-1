''' MoneyBox '''
'''


Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку

При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.

'''

class MoneyBox:
    #count = 0
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        
        
    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if (self.count + v) <= self.capacity:
            print(f'You can add {v} coins')
            return True
        else:
            print(f'You can not add {v} coins! Too large!')
            return False
        
    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.count += v
            print(f'{v} coins added!')
        else:
            print(f'No space available for {v} coins')

mb1 = MoneyBox(100)
mb1.can_add(40)
mb1.add(40)
mb1.can_add(50)
mb1.add(50)
mb1.can_add(60)
mb1.add(60)
