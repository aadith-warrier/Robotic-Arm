import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import dh_params as dh
import numpy as np

theta, theta2 = 34, 22
alpha, alpha2 = 0, 0
theta_step = theta/100
alpha_step = alpha/100
theta2_step = theta2/100
alpha2_step = alpha2/100   

x_data1 = []
y_data1 = []
x_data2 = []
y_data2 = []

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 4)
line1, = ax.plot(0, 0)
line2, = ax.plot(0,0)
def animate(i):
    point1 = [0,0,0]
    
    z1,x1 = (dh.generate_dh_matrices(1.2,alpha_step*i,0,theta_step*i))
    point2=dh.transform([z1,x1])
    
    z2,x2 = (dh.generate_dh_matrices(1.6, alpha2_step*i,0,theta2_step*i))   
    point3=dh.transform([z1,x1,z2,x2])
    
    print ("End effector position: ", point3, '\n', "step =" , i)
    
    line1.set_xdata([point1[0],point2[0]])
    line1.set_ydata([point1[1], point2[1]])
    
    line2.set_xdata([point2[0],point3[0]])
    line2.set_ydata([point2[1], point3[1]])
    
    return line1, line2

ani = FuncAnimation(fig, func=animate, frames=np.arange(0, 101, 1), interval=10, repeat = False)
plt.show()
    
