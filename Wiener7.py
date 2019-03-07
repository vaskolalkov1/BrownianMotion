# Geometric Brownian Motion with Varying Sigma

import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np


T = 10     # horizon
n = 500     # number of steps to make
d = T/n     # time length between successive steps

mu = 0.1        # drift parameter
sigma_range = np.arange(0.01, 0.06, 0.01)
l = len(sigma_range)

t = np.linspace(0.0, n*d, n)     # creating the time vector

r = norm.rvs(size=(l,n), scale=sqrt(d))
# r = norm.rvs(size=n, scale=sqrt(d))

W = np.empty(l)
X = np.empty(l)

W = np.empty((l,n))
X = np.empty((l,n))
for i in range(l):
    # Choose between only taking one random path, or multiple.
    # W[i] = np.cumsum(r)
    W[i] = np.cumsum(r[i])

    X[i] = (mu - 0.5 * sigma_range[i] ** 2) * t + sqrt(sigma_range[i]) * W[i]

S0 = 15
S = S0 * np.exp(X)

print(W)

for el in S:
    plt.plot(t, el)
plt.legend(sigma_range)
plt.show()