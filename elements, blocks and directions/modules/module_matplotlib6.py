#mathplotlib 6

from pylab import *

x = arange(1, 19, 3)
y = x ** 3
z = y ** 0.8

print(*x)
print(*y)
print(*z)

fig, axes = plt.subplots(figsize=(12, 5))
axes.plot(x, y, 'b')
show()
