import dh_params as dh
import inverse_kinematics as ik
import math as m 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

errors_link1=[]
errors_link2=[]

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 2.8)
ax.set_ylim(0, 2)
line1, = ax.plot(0, 0)
line2, = ax.plot(0,0)

# S= 2m, h = 1m

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

def path_linear(gamma):
    x = 1.5 + m.cos(gamma)
    y = 0.5
    return x, y

def path_circular(gamma):
    x = 1.5 + m.cos(gamma)
    y = 0.5 - 0.5*m.sin(gamma)
    return x, y

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

def motion_linear(gamma, l1=1.2, l2=1.6):
    if gamma<m.pi:
    
        x,y = path_linear(gamma)
    
        position = [x,y]
    
        theta1, theta2 = ik.inverse_kinematics(position, l1, l2)
        point1 = [0,0,0] 
    
        z1,x1 = (dh.generate_dh_matrices(1.2,0,0,theta1))
        point2=dh.transform([z1,x1])
    
        z2,x2 = (dh.generate_dh_matrices(1.6, 0,0,theta2))
        point3=dh.transform([z1,x1,z2,x2])
    
        line1.set_xdata([point1[0],point2[0]])
        line1.set_ydata([point1[1], point2[1]])
    
        line2.set_xdata([point2[0],point3[0]])
        line2.set_ydata([point2[1], point3[1]])
     
        errors_link1.append((((1.2-m.dist(point1, point2))/1.2 * 100)))
        errors_link1.append((((1.6-m.dist(point2, point3))/1.6 * 100)))
     
    return line1, line2

def motion_circular(gamma, l1=1.2, l2=1.6):
    if gamma>m.pi:
        
        x,y = path_circular(gamma)
        
        position = [x,y]
        
        theta1, theta2 = ik.inverse_kinematics(position, l1, l2)
        point1 = [0,0,0] 
        
        z1,x1 = (dh.generate_dh_matrices(1.2,0,0,theta1))
        point2=dh.transform([z1,x1])
        
        z2,x2 = (dh.generate_dh_matrices(1.6, 0,0,theta2))
        point3=dh.transform([z1,x1,z2,x2])
        
        line1.set_xdata([point1[0],point2[0]])
        line1.set_ydata([point1[1], point2[1]])
        
        line2.set_xdata([point2[0],point3[0]])
        line2.set_ydata([point2[1], point3[1]])
        
        errors_link1.append((((1.2-m.dist(point1, point2))/1.2 * 100)))
        errors_link2.append((((1.6-m.dist(point2, point3))/1.6 * 100)))
     
    return line1, line2

ani_2 = FuncAnimation(fig, func=motion_linear, frames=np.arange(0, 6.28, 0.1), interval=1, repeat = False)
ani_1 = FuncAnimation(fig, func=motion_circular, frames=np.arange(2.355,6.306,0.025), interval=4, repeat = False)    
plt.grid(axis='both')
plt.show()

print(max(errors_link1), max(errors_link2))