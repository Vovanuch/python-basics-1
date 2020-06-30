''' class. 3. '''

class Counter:
    def __init__(self, start = 0):
        self.count = start
    
print(Counter)
print(type(Counter))

print('Create x object, class Counter')
x = Counter()
print(x.count)
x.count += 1
print(x.count)
print()
print('Create y object, class Counter, default value of count is 5')
y = Counter(5)
print(y.count)
y.count += 1
print(y.count)
