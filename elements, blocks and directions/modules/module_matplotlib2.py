#matplotlib 2

from pylab import *
a = linspace(0, 5, 5)
b = a ** 2
print(a)
print(b)

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(a, b, 'b')
axes.set_xlabel('a')
axes.set_ylabel('b')
axes.set_title('title')
show()
