# One Path of Brownian Motion 1

from math import sqrt
from scipy.stats import norm
import numpy as np
from pylab import plot, show

T = 10.0
n = 500
d = T/n

x = 0.0
path = [x]

for i in range(n):
    x += norm.rvs(scale=sqrt(d))
    path.append(x)

time = np.linspace(0.0, n*d, n)

# print(path)
plot(time, path)
show()