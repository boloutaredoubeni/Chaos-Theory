"""
Boloutare Doubeni
Math 532H - Non Linear Dynamics and Chaos with Applications
September 22, 2014

Strogatz Exercise 2.8.2b

f(x) = 1-x^2
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#args for linspace
xmax = 4.
xmin = -3.
xn = 32

tmin = -3.
tmax = 4.

#the grid for the plot
x = np.linspace(xmin, xmax, xn) #the x-axis
t = np.linspace(tmin, tmax, xn) #the t-axis
XX, YY = np.meshgrid(t, x) 

def f(x,t): return 1 - pow(x,2)

x0 = [-2.,-1., 0.,1., 2] #The initial conditions
F = integrate.odeint(f,x0, t) #The solution of f(x)
dx = 1 - pow(x,2) #x'=x
dt = np.ones(xn) 
r = (dx**2 + dt**2)**0.5; #use to normalize the vectors
pt = dt/r
px = dx/r

def plot1(): 

    plt.figure(3)
    
    #plot the vector field
    plt.quiver(XX, YY, pt, 1/x)
    
    #plot labels
    plt.xlabel('$t$')
    plt.ylabel('$x$')
    plt.title('The direction field of $f(x)=1-x^{2}$')
    
    #plot limits
    plt.xlim([tmin, tmax])
    plt.ylim([xmin, xmax])
    
    #save the figure as a jpg file
    #plt.savefig('figures/Sec2_8bVec.jpg')
    plt.show()

def plot2():

    plt.figure(4)

    #plot the solution
    plt.plot(t, F)
    
    #plot labels
    plt.xlabel('$t$')
    plt.ylabel('$x$')
    plt.title('$\dot{x}=1-x^{2}$ and its solution')
    
    #plot limits
    plt.xlim([tmin, tmax])
    plt.ylim([xmin, xmax])
    
    #save the figure as a jpg file
    plt.savefig('figures/Sec2_8bSlope.jpg')
    
plot1(); plot2();

    

    



