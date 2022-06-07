import numpy as np

l1 = float(1.2)
l2 = float(1.6)
theta1 = float(34.00)
theta2 = float(22.00)
theta2 = theta1+theta2


lengths = np.array([l1, l2])
angles = np.array([theta1,theta2])
angles = angles*0.0174533

x = np.dot(lengths,np.cos(angles).T)
y = np.dot(lengths,np.sin(angles).T)

print(x,y)
