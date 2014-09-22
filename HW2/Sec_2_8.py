import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


xmax = 3.
xmin = -xmax
x_n = 9000

t = np.linspace(xmin, xmax, x_n)
x = t
x_0 = [-3.,-1., 1., 3]

def f0(x, t): return x 
def f1(x, t): return 1-pow(x,2)
X0 = odeint(f0, x_0, t)
X1 = odeint(f1, x_0, t)

plt.figure(1)
plt.axhline(); plt.axvline()
plt.plot(t, f0(x,t), label="$\dot{x}=x$")

#fix legend, if-else
plt.plot(t, X0, label="$x(t)=x(0)e^{t}$")
plt.legend()

plt.show()

plt.figure(2)
plt.axhline(); plt.axvline()
plt.plot(t, f1(x,t), label="\dot{x}=1-x^{2}")

plt.plot(t, X1, label="")
