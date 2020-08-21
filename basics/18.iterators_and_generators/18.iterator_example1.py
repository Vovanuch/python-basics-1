class Any:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for i in self.iterable:
            if i != 2:
                yield i


list_a = [1, 2, 3]
obj = Any(list_a)
list_b = list(obj)

print(list_a)
print(obj)
print(list_b)
