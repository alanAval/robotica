import numpy as np
import veltrans as vel
l1 = 0
l2 = 0.65

def jacobian(theta):
    s2 = np.sin(theta[1])
    s3 = np.sin(theta[2])
    c2 = np.cos(theta[1])
    c3 = np.cos(theta[2])
    return np.array([
        [(l1*s2*c3) + (l1*c2*s3) + (l2*s3), l2*s3, 0],
        [(-l1*s2*s3) + (l1*c2*c3) + (l2*c3), l2*c3, 0],
        [0, 0, 0]])



theta1 = 0
theta2 = 16.28
theta3 = 30

j = jacobian(np.array([theta1, theta2, theta3]) * np.pi / 180)
print(j)

vrelw = j @ np.array([20, -10, 12])
print(vrelw)


trelw = np.array([[np.sqrt(3)/2, np.sqrt(1)/2, 0, 0.1], 
               [-(np.sqrt(1)/2), np.sqrt(3)/2, 0, 0.2],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

vrelt = vel.veltrans(trelw, np.array([vrelw[0], vrelw[1], 0, 0, 0, vrelw[2]]))

print(vrelt)


















