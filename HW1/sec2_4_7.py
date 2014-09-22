"""
Linear Stability Analysis
"""

import numpy as np
import matplotlib.pyplot as plt

a = 2

def f(x): return a*x-pow(x,3)

x = np.linspace(-1.,.1)

plt.figure()
plt.plot(x, f(x))
plt.axhline()
#x1_, x2_ = plt.plot(0, 0, marker='o'), plt.plot(-np.sqrt(a),0, marker='o')

#t1, t2 = plt.arrow(0, 0, -np.sqrt(a), 0), plt.arrow(0, 0, -np.sqrt(a), 0)

plt.show()
