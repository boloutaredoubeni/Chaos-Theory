"""
Given the fixed points fing the equation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
             

def f(x,t):return x * (x + 1) * (x - 2)

x0 = np.linspace(-3.,-1.)
x1 = np.linspace(-1.,0)
x2 = np.linspace(0,2)
x3 = np.linspace(2,3)

xn = np.linspace(-3.,3)



x_int = np.array([-1.1,0.1,2.9])
X = odeint(f, x_int, xn )

plt.figure()
plt.plot(x0, f(x0, x_int),
        x1, f(x1, x_int), 
        x2, f(x2, x_int), 
        x3, f(x3, x_int))
        
plt.xlabel(r'$x(t)$')
plt.ylabel(r'$\dot{x}$')
plt.axhline()
plt.show()

