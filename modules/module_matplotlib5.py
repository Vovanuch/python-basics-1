#mathplotlib 5

from pylab import *

x = arange(1, 19, 3)
y = x ** 3
z = y ** 0.8

print(*x)
print(*y)
print(*z)

fig, axes = plt.subplots(nrows = 1, ncols = 3)

for ax in axes:
	ax.plot(x, y, 'r')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_title('title')
	
fig.tight_layout()
show()
