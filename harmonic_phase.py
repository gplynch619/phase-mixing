import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

m = 1.
w = 1.

#This defines the physical system. gc is a vector of generalized coordinates, in this case position and momentum.
#t is the independent variable, for most systems this will be time. 
#The system function returns the vector of derivatives dq/dt and dp/dt

def hoscillator(gc, t, mass, omega):
    qtemp, ptemp = gc
    q = qtemp*mass*omega
    p = ptemp/(mass*omega)
    derivative = [omega*p, -omega*q]
    return derivative

gcq0 = input("What is the intiial 'q' coordinate?")
gcp0 = input("What is the intiial 'p' coordinate?")

gc0=[gcq0, gcp0]

t = np.linspace(0, 10, 101)

sol = odeint(hoscillator, gc0, t, args=(m, w))

fig, ax= plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]})

ax[0].plot(sol[:,0], sol[:,1])

ax[0].grid(True)
ax[0].set_xlabel('q')
ax[0].set_ylabel('p')

ax[0].axhline(y=0, color='k')
ax[0].axvline(x=0, color='k')

dot, = ax[0].plot(sol[0,0], sol[0,1], 'o')
osc, = ax[1].plot(sol[0,0], 0, 'o')

def init():
    dot.set_data([],[])
    osc.set_data([],[])
    return dot, osc

def animate(i):
    q = sol[i,0]
    p = sol[i, 1]
    dot.set_data(sol[i, 0], sol[i,1])
    osc.set_data(sol[i,0], 0)
    return dot, osc 

ax[1].set_xlim([-1.1, 1.1])
ax[1].set_ylim([-0.1, 0.1])
ax[1].get_xaxis().set_ticks([])
ax[1].get_yaxis().set_ticks([])


fps=15.0
mult=(1.0/fps)*1000
frames = 101

anim = FuncAnimation(fig, animate, init_func=init, frames=frames, interval=mult, blit=False)
anim.save('test.gif', dpi=80, writer='imagemagick')

plt.show()
