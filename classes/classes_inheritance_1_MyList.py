''' Классы. Наследование (inheritance). Расширенный список. Добавили метод, проверяющий, является ли список чётной длины'''

class MyList(list):
    def even_length(self):
        return (len(self) % 2) == 0
        
x = MyList()
print(x)
x.extend([1, 2, 3])
print(x)
print('Количество элементов чётное?', x.even_length())
x.append(4)
print(x)
print('Количество элементов чётное?', x.even_length())
