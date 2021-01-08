#numpy + mathplotlib 7

from numpy import *
from pylab import *

n = randn(100000)
#fig, axes = plt.subplots(1, 2, figsize = (12, 5))
fig, axes = plt.subplots(nrows = 1, ncols = 2)

for i in range(len(axes)):
	axes[i].hist(n)

'''
axes[0] = hist(n)
#axes[0].set_title('Default histogram')
#axes[0].set_xlim((min(n), max(m)))
#axes[0].plot()

axes[1] = hist(n, cumulative = True, bins = 50)
#axes[1].set_title('Cumulative histogram')
#3333333axes[1].set_xlim((min(n), max(m)))
#axes[1].plot()'''



show()
