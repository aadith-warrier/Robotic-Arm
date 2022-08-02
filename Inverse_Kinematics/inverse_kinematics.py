import math as m

def inverse_kinematics(position, l1, l2):
    x = position[0]
    y = position[1]
    r_squared = x**2 + y**2
    r = m.sqrt(r_squared)
    theta2 = -m.pi + m.acos((l1**2 + l2**2 - r_squared)/(2*l1*l2))
    theta1 = m.atan(y/x) + m.acos((r_squared+l1**2 - l2**2)/(2*r*l1))
    conversion = 180/m.pi
    return theta1*conversion, theta2*conversion