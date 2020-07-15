''' Based and derived classes  '''

class Base:
    def __init__(self):
        self.val = 0
        
    def add_one(self):
        self.val += 1
    
    def add_more(self, x):
        for i in range(x):
            self.add_one()


class Derived(Base):
    def add_one(self):
        self.val += 10



print('Создадим х класса Base, сделаем с ним операции.')
my_x = Base()
print('my_x.val =', my_x.val)
print('Добавим единицу')
my_x.add_one()
print('my_x.val =', my_x.val)
print('Добавим 4')
my_x.add_more(4)
print('my_x.val =', my_x.val)

print('Создадим y класса Derived, сделаем с ним операции.')

my_y = Derived()
print('my_y.val =', my_y.val)
print('Функция add_one должна добавить 10, а не 1.')
my_y.add_one()
print('my_y.val =', my_y.val)
my_y.add_more(3)
print('my_y.val =', my_y.val)
