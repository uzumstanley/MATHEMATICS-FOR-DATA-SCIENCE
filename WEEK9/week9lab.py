# -*- coding: utf-8 -*-
"""WEEK9LAB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c-1IG57r1F6weSdvR9VulSQPAxoWfTVh
"""

import numpy as np
from scipy import stats
import math as mt
import random as rnd

X = stats.binom(40, 0.5) # Decclare X to be a binomial random variable

print (X.pmf(3)) # p(X = 3) which implies we are calculating the mass function for the third trial

print (X.cdf(4)) # p(X <= 4) which implies we are calculating the mass function for upto fourth trial

print (X.mean())     # Mean

print (X.var())    # Variance

print (X.std())   # Standard Deviation

QUESTION 1 SOLUTION

import numpy as np
from scipy import stats
import math as mt
import random as rnd

X = stats.binom(5, 0.8)

print (X.pmf(5))

print (X.cdf(5))

print (X.mean())

print (X.var())

print (X.std())

Generating Goemetric Distribution

from scipy.stats import geom
import matplotlib.pyplot as plt

# X = Discrete random variable representing number of throws
# p = Probability of the perfect throw

# Calculating for p = 1
X = 1,2,3,4,5
p = 0.04

# Calculating geometric probability distribution
geom_pd = geom.pmf (X, p)

# plot the probability distribution
fig, ax = plt.subplots (1, 1, figsize=(8, 6))
ax.plot (X, geom_pd, 'bo', ms=8, label='geom pmf')
plt.xlabel ("X - No. of Throws", fontsize="18")
plt.ylabel ("Probability", fontsize="18")
plt.title ("Geometric Distribution - No. of Throws Vs Probability",
           fontsize="18")
ax.vlines (X, 0, geom_pd, colors='b', lw=5, alpha=0.5)



QUESTION 2 SOLUTION

from scipy.stats import geom
import matplotlib.pyplot as plt

# X = Discrete random variable representing number of voter try
# p = Probability of success

# Calculating for p = 1
X = 3
p = 0.2

# Calculating geometric probability distribution
geom_pd = geom.pmf (X, p)

# plot the probability distribution
fig, ax = plt.subplots (1, 1, figsize=(8, 6))
ax.plot (X, geom_pd, 'bo', ms=8, label='geom pmf')
plt.xlabel ("X - No. of Voter try", fontsize="18")
plt.ylabel ("Probability", fontsize="18")
plt.title ("Geometric Distribution - No. of Voter try Vs Probability",
           fontsize="18")
ax.vlines (X, 0, geom_pd, colors='b', lw=5, alpha=0.5)