import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m = 1.
w = 1.

#This defines the physical system. gc is a vector of generalized coordinates, in this case position and momentum.
#t is the independent variable, for most systems this will be time. 
#The system function returns the vector of derivatives dq/dt and dp/dt

def hoscillator(gc, t, mass, omega):
    qtemp, ptemp = gc
    q = qtemp*np.sqrt(mass*omega)
    p = ptemp/np.sqrt(mass*omega)
    derivative = [omega*p, -omega*q]
    return derivative

gcq0 = input("What is the intiial 'q' coordinate?")
gcp0 = input("What is the intiial 'p' coordinate?")

gc0=[gcq0, gcp0]

t = np.linspace(0, 10, 101)

sol = odeint(hoscillator, gc0, t, args=(m, w))

fig, ax= plt.subplots()

ax.plot(sol[:,0], sol[:,1])

ax.grid(True)
ax.set_xlabel('q')
ax.set_ylabel('p')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.show()
