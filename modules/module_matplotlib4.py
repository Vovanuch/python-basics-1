#mathplotlib 4

from pylab import *

x = arange(1, 19, 3)
y = x ** 3
z = y ** 0.8

print(*x)
print(*y)
print(*z)

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.3])

axes1.set_xlabel('x')
axes1.set_ylabel('y')

axes2.set_xlabel('x')
axes2.set_ylabel('z')


axes1.plot(x, y , 'r')
axes2.plot(x, z , 'y')

show()
