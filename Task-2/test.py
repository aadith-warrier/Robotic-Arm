import simulation as sim
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math as m

fig, ax = plt.subplots()
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
line1, = ax.plot(0, 0)

def path(gamma):
    
    if gamma>m.pi:
        #linear path
        x = 1.5 - m.cos(gamma)
        y = 1.5
    else:
        #circular path
        x = 1.5 - m.cos(gamma)
        y = 1.5 + m.sin(gamma)
        
    line1.set_xdata([0,x])
    line1.set_ydata([0,y])
    
    return line1
    

ani = FuncAnimation(fig, func=path, frames=np.arange(0, 6.28, 0.1), interval=100)
plt.show()
