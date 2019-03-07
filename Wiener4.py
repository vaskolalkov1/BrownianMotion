# One Path of Geometric Brownian Motion 1

# Assume the stock price follows a geometric Brownian motion.
# dS = (mu * S(s))ds + (sigma*S(s))dW(s)
# The standard Brownian motion is denoted as W(t).
# This means that the solution is the following: S(t)=S(0)*exp{(mu-0.5*sigma^2)*t + sigma*W(t)}.

# Let X(t)=(mu-0.5*sigma^2)*t + sigma*W(t). Then we have S(t)=S(0)*exp{X(t)}.
# Thus, we first calculate the standard Brownian motion W(t), then we get the process X(t), and finally S(t).

import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import norm
import numpy as np
# from pylab import plot, show

T = 2.0    # horizon
n = 500     # number of steps to make
d = T/n     # time length between successive steps

mu = 0.1        # drift parameter
sigma = 0.01    # volatility parameter

t = np.linspace(0.0, n*d, n)     # creating the time vector

# First, we create standard Brownian motion.
r = norm.rvs(size=n, scale=sqrt(d))     # generating a sequence of standard normal random variables
W = np.cumsum(r)                                # summing the normal increments and saving them to the sample path

# Now, we construct the process X(t).
X = (mu - 0.5*sigma**2)*t + sqrt(sigma)*W

# We obtain the path for the price process S(t).
S = np.empty(n)                  # sample paths of stock price
S0 = 15                          # starting price
S = S0*np.exp(X)


plt.plot(t, S)
plt.show()
