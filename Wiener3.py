# Multiple Paths of Brownian Motion 1

import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np
# from pylab import plot, show

sigma = 2   # parameter of the Brownian motion
T = 10.0    # horizon
n = 1000     # number of steps to make
d = T/n     # time length between successive steps
m = 5       # number of sample paths to realize

paths = np.empty((m,n))                  # sample paths of the Brownian motion
time = np.linspace(0.0, n*d, n)     # creating the time vector
out = np.empty(n)

for i in range(m):
    x = 0.0  # starting point
    x = np.asarray(x)  # creating an array
    r = norm.rvs(size=n, scale=sqrt(d)*sigma)  # generating a sequence of standard normal random variables
    np.cumsum(r, out=out)  # summing the normal increments and saving them to the sample path
    paths[i,:] = out
    plt.plot(time, paths[i])

plt.show()
