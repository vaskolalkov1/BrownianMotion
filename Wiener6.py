# Multiple Paths of Geometric Brownian Motion 2

import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np


T = 10     # horizon
n = 500     # number of steps to make
d = T/n     # time length between successive steps
m = 1       # number of observations to produce

mu = 0.1        # drift parameter
sigma = 0.01    # volatility parameter

t = np.linspace(0.0, n*d, n)     # creating the time vector

r = norm.rvs(size=(m,n), scale=sqrt(d))

W = np.empty((m,n))
X = np.empty((m,n))
for i in range(m):
    W[i] = np.cumsum(r[i])
    X[i] = (mu - 0.5 * sigma ** 2) * t + sqrt(sigma) * W[i]

S0 = 15
S = S0 * np.exp(X)

print(W)

for el in S:
    plt.plot(t, el)
plt.show()