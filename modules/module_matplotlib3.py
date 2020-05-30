#mathplotlib 3

from pylab import *

x = arange(1, 19, 3)
y = x * 3
z = y ** 0.8

print(*x)
print(*y)
print(*z)

#axes1 = plt.figure()
plot(x, y , 'y')
plot(x, z , 'b')
show()
