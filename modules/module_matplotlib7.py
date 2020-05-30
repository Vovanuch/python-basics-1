#mathplotlib 7

from pylab import *

x = arange(1, 19, 3)
y = x ** 3
z = y ** 0.8

print(*x)
print(*y)
print(*z)

fig, ax = plt.subplots()
ax.plot(x, x**2, label = 'x**2')
ax.plot(x, x**3, label = 'x**3')
ax.legend(loc = 2)

ax.set_xlabel('x')
ax.set_ylabel('x**n')
ax.set_title('exponenta')
show()
