''' class. 4.'''
class Counter:
    def __init__(self, start = 10):
        self.count = start
        
    def inc(self, val = 1):
        self.count += val
        
    def reset(self):
        self.count = 0
        
    def set(self, val = 0):
        self.count = val
        

x = Counter(15)
print('x.count = ', x.count)
x.inc()
print('x.count = ', x.count)
x.inc(10)
print('x.count = ', x.count)
x.reset()
print('x.count = ', x.count)
x.set(50)
print('x.count = ', x.count)
