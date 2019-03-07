# One Path of Brownian Motion 2

# import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np
from pylab import plot, show

sigma = 2   # parameter of the Brownian motion
T = 10.0    # horizon
n = 500     # number of steps to make
d = T/n     # time length between successive steps

path = np.empty(n)                  # sample path of the Brownian motion
time = np.linspace(0.0, n*d, n)     # creating the time vector

x = 0.0             # starting point
x = np.asarray(x)   # creating an array

r = norm.rvs(size=n, scale=sqrt(d)*sigma**2)    # generating a sequence of standard normal random variables
np.cumsum(r, out=path)                          # summing the normal increments and saving them to the sample path

plot(time, path)
show()