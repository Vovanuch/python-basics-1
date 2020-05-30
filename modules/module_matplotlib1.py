#matplotlib

from pylab import *
a = linspace(0, 5, 5)
b = a ** 2
print(a)
print(b)

figure()
plot(a, b, 'r')
xlabel('a')
ylabel('b')
title('title')
show()
