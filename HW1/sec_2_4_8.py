"""
Gompertz model for Tumor growth
"""
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt

a, b = 1, 1

def f(N): return -a * N * np.log(b*N)
f_prime = derivative(f, 1e-3, dx=1e-6), derivative(f, 1, dx=1e-6)
print f_prime


t = np.linspace(1e-3, 10.)
plt.plot(t, f(t))
plt.axhline()
plt.axis('equal')
plt.show()


