import numpy as np

l1 = float(input("Length of first link: "))
l2 = float(input("Length of the second link: "))
theta1 = float(input("Incliation of the first link: "))
theta2 = float(input("Inclination of the second link: "))
theta2 = theta1+theta2


lengths = np.array([l1, l2])
angles = np.array([theta1,theta2])
angles = angles*0.0174533

x = np.dot(lengths,np.cos(angles).T)
y = np.dot(lengths,np.sin(angles).T)

print(x,y)
