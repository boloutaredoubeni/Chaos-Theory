"""
Boloutare Doubeni
Math 532H - Non Linear Dynamics and Chaos with Applications
September 22, 2014

Strogatz Exercise 2.8.2a

f(x) = x
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#args for linspace
xmin = 0.
xmax = 10.
xn = 32

tmin = xmin
tmax = xmax

#the grid for the plot
x = np.linspace(xmin, xmax,xn) #the x-axis
t = np.linspace(0, 2*xmax,xn) #the t-axis
XX, YY = np.meshgrid(t, x) 
