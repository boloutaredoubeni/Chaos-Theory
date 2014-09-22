"""
Math 532H - Homework
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import sin, cos
from scipy.optimize import fixed_point

#the parameters
xmax = 8.
xmin = -xmax
t = np.linspace(xmin,xmax)
x_dot = plt.plot(t, sin(t), label="$\dot{x}=\sin(x)$")
x_ddot =plt.plot(t, cos(t), label="$\ddot{x}=\cos(x)$")

plt.figure()
plt.axhline(); plt.axvline()

#Customizition
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$\dot{x}$')
plt.title(r'The flow of $f(x)$ and its acceleration')


#Traditional axis
#plt.axhline();plt.axvline()
plt.axis('equal')

plt.axes()

x_dot.show()
x_ddot.show()