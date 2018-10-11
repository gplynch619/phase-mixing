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

gc0 = [0, 0]

t = np.linspace(0, 10, 101)

sol = odeint(hoscillator, gc0, t, args=(m, w))

plt.plot(sol[:,0], sol[:,1])

plt.legend(loc='best')
plt.xlabel('q')
plt.ylabel('p')
plt.show()
