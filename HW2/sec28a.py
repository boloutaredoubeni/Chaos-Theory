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
xmin = -5
xmax = 10.
xn = 32

tmin = 0
tmax = 2*xmax

#the grid for the plot
x = np.linspace(xmin, xmax, xn) #the x-axis
t = np.linspace(tmin, tmax, xn) #the t-axis
XX, YY = np.meshgrid(t, x) 

    
def f(x,t): return x #f(x)=x

x0 = [-1.,0.,.1,.5,1.,1.5] #The initial conditions
F = integrate.odeint(f,x0, t) #The solution of f(x)
dx = x #x'=x
dt = np.ones(xn) 
r = (dx**2 + dt**2)**0.5; #use to normalize the vectors
pt = dt/r
px = dx/r

def plot1(): 
    
    plt.figure(2)
    
    #plot the vector field
    plt.quiver(XX, YY, pt, px)
    
    #plot labels
    plt.xlabel('$t$')
    plt.ylabel('$x$')
    plt.title('The direction field of $f(x)=x$')
    
    #plot limits
    plt.xlim([tmin, tmax])
    plt.ylim([xmin, xmax])
    
    plt.show()
    #plt.savefig('figures/Sec2_8aSlope.jpg')
   
   

def plot2():
    plt.figure(1)
    
    #plot the solution
    plt.plot(t, F)
    
    #plot labels
    plt.xlabel('$t$')
    plt.ylabel('$x$')
    plt.title('$\dot{x}=x$ and its solution')
    
    #plot limits
    plt.xlim([tmin, tmax])
    plt.ylim([xmin, xmax])
    
    #save the figure as a jpg file
    plt.plot()
    #plt.savefig('figures/Sec2_8aVec.jpg')


plot1(); plot2();

