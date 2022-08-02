#Defining Matrices and related operations

import numpy as np
import math

def generate_dh_matrices(a, alpha, d, theta):
    
    alpha *= 0.017444
    theta *= 0.017444

    #joint transform
    z = np.zeros((4,4))
    z[0][0] = math.cos(theta)
    z[1][1] = math.cos(theta)
    z[0][1] = -math.sin(theta)
    z[1][0] = math.sin(theta)
    z[2][2] = 1
    z[2][3] = d
    z[3][3] = 1

    #link transform
    x = np.zeros((4,4))
    x[0][0] = 1
    x[0][3] = a
    x[1][1] = math.cos(alpha)
    x[1][2] = -math.sin(alpha)
    x[2][1] = math.sin(alpha)
    x[2][2] = math.cos(alpha)
    x[3][3] = 1
    
    return z,x

def transform(array):
    t = np.linalg.multi_dot(array)
    return [t[0][3],t[1][3],t[2][3]]

    