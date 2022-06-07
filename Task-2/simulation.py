import dh_params as dh
import inverse_kinematics as ik
import math as m 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2.8, 2.8)
ax.set_ylim(0, 2.8)
line1, = ax.plot(0, 0)
line2, = ax.plot(0,0)

def path(gamma):
    
    if gamma>m.pi:
        #linear path
        x = 1.5 - m.cos(gamma)
        y = 0.5
    else:
        #circular path
        x = 1.5 - m.cos(gamma)
        y = 0.5 + m.sin(gamma)
    
    return x,y

def motion(gamma, l1=1.2, l2=1.6):
    
    x,y = path(gamma)
    
    position = [x,y]
    print('position:', x, y, "\n")
    
    theta1, theta2 = ik.inverse_kinematics(position, l1, l2)
    print('angles:' , theta1, theta2)
    point1 = [0,0,0] 
    
    z1,x1 = (dh.generate_dh_matrices(1.2,0,0,theta1))
    point2=dh.transform([z1,x1])
    
    z2,x2 = (dh.generate_dh_matrices(1.6, 0,0,theta2))
    point3=dh.transform([z1,x1,z2,x2])
    
    line1.set_xdata([point1[0],point2[0]])
    line1.set_ydata([point1[1], point2[1]])
    
    line2.set_xdata([point2[0],point3[0]])
    line2.set_ydata([point2[1], point3[1]])
     
    return line1, line2

ani = FuncAnimation(fig, func=motion, frames=np.arange(0, 6.28, 0.1), interval=100)
plt.show()


