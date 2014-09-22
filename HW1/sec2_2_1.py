"""
Graphically analyze 
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import cos
from scipy.integrate import odeint

xmax = 10.
xmin = -xmax
x = np.linspace(xmin, xmax)
t = x
def f(x,t): return 1 + 0.5*cos(x)
y_0 = np.array([-1., 0., 1., np.pi])
y = odeint(f,y_0, t)


#the vector field on the real line is pointed right
plt.plot(x, f(x,t), label=r'$\dot{x}=1+\frac{1}{2}\cos{x}$')
plt.plot(x, y, label=r'$f(x)=x$')
plt.legend()
plt.show()