"""
Strogatz 3.1.1
"""

from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy.solvers import solve
from sympy.abc import x

xmax = 13.
xmin = -xmax
xasy = 1e-0

rmax = 3.
rmin = -rmax

"""
CONSTRUCT A RECURSIVE WHILE-LOOP TO ESTIMATE THE BIFURCATION
?Binary Search?

Hint ANS: 2
"""
#r = 0
eq1 = 1 + pow(x,2)
rzero = solve(eq1, x)

#r < 0
eq2 = 1 - rmin*x + pow(x,2)
rneg = solve(eq2, x)

#r > 0
eq3 = 1 + rmax*x + pow(x,2)
rpos = solve(eq3, x)

#f(x)=1+rx+x^2
def f(x,r): return 1 + r*x + pow(x,2)
t = np.linspace(xmin, xmax)
t1 = np.linspace(xmin, -xasy)
t2 = np.linspace(xasy, xmax)

def r(x): return -x-1/x

#FIGURE 1
plt.figure("Vector Field")
plt.plot(t, f(t,rmin), label=r"$r<0$" ); 
plt.plot(t, f(t,0), label=r"$r=0$") 
plt.plot(t, f(t,rmax), label=r"$r>0$")
#find a way to accept a list of r_args are parameters for multiple plots of f(x)
#possibly try 3 sub-plots

plt.axhline()
plt.legend()
plt.show()

#create a textbox for the results
print(rpos, rzero, rneg)

#FIGURE 2
plt.figure("Bifurcation")
plt.plot(t1, r(t1), t2, r(t2), -t, t) #plot me without my asymptotes
plt.axhline()
plt.axis('equal')

plt.show()
